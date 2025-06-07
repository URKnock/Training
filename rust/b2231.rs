use std::io::stdin;

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

// 2231: 분해합

fn main() -> Result<()> {
	let mut input = String::new();
	stdin().read_line(&mut input).expect("failed: input");
    let n : usize = input.trim().parse().expect("failed: parse");

	let mut result = 0;
    for i in 0..n+1 {
    	let mut num = i;
		let mut count = num;

		while num > 0 {
			count += num % 10;
			num /= 10;
		}

		if count == n {
			result = i;
			break;
		}
    }
	print!("{result}");

	Ok(())
}