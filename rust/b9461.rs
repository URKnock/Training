use std::io::stdin;
use std::fmt::Write;

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

// 9461: 파도반 수열

fn solution(dp: &mut [usize], n: usize) {
	for i in 3..n {
		dp[i] = dp[i-2] + dp[i-3];
	}
}

fn main() -> Result<()> {
	let mut output = String::new();
	let mut input = String::new();
	stdin().read_line(&mut input).expect("failed: input");
    let t : usize = input.trim().parse().expect("failed: parse");

    for i in 0..t {
		input = String::new();
		stdin().read_line(&mut input).expect("failed: input");
	    let n : usize = input.trim().parse().expect("failed: parse");
	    let mut dp: Vec<usize> = Vec::with_capacity(n);
	    for j in 0..3 {
	    	dp.push(1);
	    }
	    for j in 3..n {
	    	dp.push(0);
	    }
	    solution(&mut dp, n);
    	writeln!(output, "{}", dp[n-1]);
    }
	print!("{output}");

	Ok(())
}