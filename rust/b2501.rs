use std::io::stdin;

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

// 2501: 약수 구하기

fn main() -> Result<()> {
	let mut input = String::new();
	stdin().read_line(&mut input).expect("failed: input");
	let num: Vec<i32> = input
		.split_whitespace()
		.filter_map(|s| s.parse().ok())
		.collect();
	let (n, k) = (num[0], num[1]);

	let mut count = 0;
	let mut result = 0;

	for i in 1..n+1 {
		if n % i == 0 {
			count += 1;
			if count == k {
				result = i;
				break;
			}
		}
	}
	println!("{result}");
	Ok(())
}