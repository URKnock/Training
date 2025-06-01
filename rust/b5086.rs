use std::io::{stdin, BufRead};
use std::fmt::Write;

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

// 5086: 배수와 약수

fn main() -> Result<()> {
	let mut output = String::new();
	for line in stdin().lock().lines() {
		let line = line.expect("failed: input");
		let num: Vec<i32> = line
			.split_whitespace()
			.filter_map(|s| s.parse().ok())
			.collect();
		let (a, b) = (num[0], num[1]);

	    if a == 0 && b == 0 {
	    	break;
	    }

	    if b % a == 0 {
	    	writeln!(output, "factor").unwrap();
	    } else if a % b == 0 {
	    	writeln!(output, "multiple").unwrap();
	    } else {
	    	writeln!(output, "neither").unwrap();
	    }
	}
	println!("{output}");
	Ok(())
}