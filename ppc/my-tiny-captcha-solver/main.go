package main

import (
	"bytes"
	"context"
	"crypto/sha256"
	"fmt"
	"github.com/fasthttp/router"
	"github.com/sergeymakinen/go-bmp"
	"github.com/valyala/fasthttp"
	clientv3 "go.etcd.io/etcd/client/v3"
	"golang.org/x/image/font"
	"golang.org/x/image/font/basicfont"
	"golang.org/x/image/math/fixed"
	"image"
	"image/color"
	"image/draw"
	"log"
	"math/rand"
	"os"
	"strconv"
	"time"
	"unsafe"
)

const letterBytes = "0123456789"
const (
	letterIdxBits = 4                    // 6 bits to represent a letter index
	letterIdxMask = 1<<letterIdxBits - 1 // All 1-bits, as many as letterIdxBits
	letterIdxMax  = 63 / letterIdxBits   // # of letter indices fitting in 63 bits
)

var src = rand.NewSource(time.Now().UnixNano())

func RandStringBytesMaskImprSrcUnsafe(n int) string {
	b := make([]byte, n)
	// A src.Int63() generates 63 random bits, enough for letterIdxMax characters!
	for i, cache, remain := n-1, src.Int63(), letterIdxMax; i >= 0; {
		if remain == 0 {
			cache, remain = src.Int63(), letterIdxMax
		}
		if idx := int(cache & letterIdxMask); idx < len(letterBytes) {
			b[i] = letterBytes[idx]
			i--
		}
		cache >>= letterIdxBits
		remain--
	}

	return *(*string)(unsafe.Pointer(&b))
}

func addLabel(img *image.Paletted, x, y int, label string) {
	col := color.RGBA{R: 0, G: 0, B: 0, A: 255}
	point := fixed.Point26_6{X: fixed.I(x), Y: fixed.I(y)}

	d := &font.Drawer{
		Dst:  img,
		Src:  image.NewUniform(col),
		Face: basicfont.Face7x13,
		Dot:  point,
	}
	d.DrawString(label)
}

func NewSHA256(data []byte) []byte {
	hash := sha256.Sum256(data)
	return hash[:]
}

func genImage() (*image.Paletted, []byte) {
	c := color.Palette{color.RGBA{R: 0, G: 0, B: 0, A: 255},
		color.RGBA{R: 255, G: 255, B: 255, A: 255}}

	img := image.NewPaletted(image.Rect(0, 0, 10000, 50), c)
	draw.Draw(img, img.Bounds(), &image.Uniform{C: color.RGBA{R: 255, G: 255, B: 255, A: 255}}, image.Point{}, draw.Src)

	text := RandStringBytesMaskImprSrcUnsafe(1000)
	// println(text)
	addLabel(img, 10, 30, text)

	return img, NewSHA256([]byte(text))
}

var (
	dialTimeout    = 2 * time.Second
	requestTimeout = 10 * time.Second
)

func GetCaptcha(ctx *fasthttp.RequestCtx) {
	KVCtx, _ := context.WithTimeout(context.Background(), requestTimeout)

	img, textHash := genImage()
	ctx.SetContentType("image/bmp")
	bmp.Encode(ctx, img)

	cptId := RandStringBytesMaskImprSrcUnsafe(50)
	ctx.Response.Header.Set("X-Captcha-Id", cptId)
	ctx.Response.Header.Set("X-Time-To-Solve", "100 seconds")

	lease, _ := cli.Grant(ctx, 100)
	kv.Put(KVCtx, cptId, string(textHash), clientv3.WithLease(lease.ID))
}

var flag = os.Getenv("TASK_FLAG")

func SubmitCaptcha(ctx *fasthttp.RequestCtx) {
	KVCtx, _ := context.WithTimeout(context.Background(), requestTimeout)

	gr, err := kv.Get(KVCtx, ctx.UserValue("cptId").(string))
	kv.Delete(KVCtx, ctx.UserValue("cptId").(string))

	if err != nil {
		panic(err)
	}
	// println(gr.Count)
	if gr.Count > 0 {
		if bytes.Equal(gr.Kvs[0].Value, ctx.PostBody()) {
			randomIndex := rand.Intn(len(flag))
			ctx.WriteString(fmt.Sprintf("Good!\nflag[%s] = %s", strconv.Itoa(randomIndex), string(flag[randomIndex])))
		} else {
			ctx.WriteString("Wrong solution! Captcha deleted from database")
		}
	} else {
		ctx.WriteString("Captcha ID doesn't exist in database")
	}
}

func Index(ctx *fasthttp.RequestCtx) {
	ctx.Write(sourceCode)
}

var sourceCode []byte
var cli *clientv3.Client
var kv clientv3.KV

func main() {
        println("Starting task")
	sourceCode, _ = os.ReadFile("main.go")

	cli, _ = clientv3.New(clientv3.Config{
		DialTimeout: dialTimeout,
		Endpoints:   []string{"etcd:2379"},
	})
	defer cli.Close()
	kv = clientv3.NewKV(cli)

	r := router.New()

	r.GET("/", Index)
	r.GET("/getCaptcha", GetCaptcha)
	r.POST("/submitCaptcha/{cptId}", SubmitCaptcha)

	println("Before start server")
	log.Fatal(fasthttp.ListenAndServe(":8080", r.Handler))

}
