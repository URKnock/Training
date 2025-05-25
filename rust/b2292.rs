use std::io;

// 2292: 벌집

fn main() {
    let mut N = String::new();
    io::stdin().read_line(&mut N).expect("failed: input");
    let N : u32 = N.trim().parse().expect("failed: parse");

	let mut count: u32 = 1;
	let mut total: u32 = 1;

	while N > total {
		total += count * 6;
		count += 1;
	}

	println!("{}", count);
}