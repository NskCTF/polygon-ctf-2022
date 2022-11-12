const arr: Array<i32> = [131, 17, 232, 321, 139, 234, 187, 263, 67, 58, 182, 238, 109, 144, 304, 232, 2, 367, 152, 321, 70, 349, 193, 174, 249, 268, 186, 324, 290, 258, 1, 276, 100, 278, 112, 327, 46, 10, 180, 270, 239, 117, 75, 137, 380, 370, 143, 274, 128, 237, 265, 226, 396, 75, 277, 30, 19, 4, 217, 192, 184, 253, 138, 133, 113, 214, 74, 74, 268, 159, 388, 38, 274, 60, 188, 3, 144, 136, 16, 19, 370, 393, 161, 18, 119, 244, 52, 327, 318, 48, 233, 330, 160, 95, 44, 3, 162, 51, 5, 94];

function A(a: i32, b: i32): i32 {
  return ((a * arr.pop() - 2110 + b ^ arr.pop())) & 0xFF;
}
function B(a: i32, b: i32): i32 {
  arr.push(b);
  return ((a * arr.pop() - 4254 + b ^ arr.pop())) & 0xFF;
}
function C(a: i32, b: i32): i32 {
  arr.push(a ^ b);
  return ((a * arr.pop() - 1294 + b ^ arr.pop())) & 0xFF;
}


export function flag(val: u32): string {
  const f_arr = new Array<i32>(9);
  f_arr[0] = 66;
  f_arr[1] = 68;
  if (val == 777) return "NOPE";
  for (let i: i32 = 2; i < f_arr.length; ++i) {
    B(f_arr[i - 1] ^ 12, f_arr[i - 2] ^ 25);
    A(val ^ 198, val ^ 666);
    f_arr[i] = (C(f_arr[i - 1] ^ f_arr[i - 2], val ^ 91) % (0x7F - 0x30)) + 0x30;
  }
  if (val == 777) return "CTF{w3b_asm_enjoy3r_" + String.fromCharCodes(f_arr) + "}";
  return "Random data, not matters what it means, really: " + String.fromCharCodes(f_arr);
}