use std::io;

// 15894: 수학은 체육과목 입니다

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("failed: input");
    let n : u32 = n.trim().parse().expect("failed: parse");
    let result = n * 4;
	println!("{result}");
}