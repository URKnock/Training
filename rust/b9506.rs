use std::io::stdin;
use std::fmt::Write;

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

// 9506: 약수들의 합

fn main() -> Result<()> {
    loop {
		let mut input = String::new();
		stdin().read_line(&mut input).expect("failed: input");
	    let n : i32 = input.trim().parse().expect("failed: parse");
    	if n == -1 {
    		break;
    	}

    	let mut data = Vec::new();
    	for i in 1..n {
    		if n % i == 0 {
    			data.push(i);
    		}
    	}
    	let mut total = 0;
    	for i in 0..data.len() {
    		total += data[i];
    		if total > n {
    			break;
    		}
    	}
		let mut output = String::new();
    	if total == n {
    		write!(output, "{} = ", n).unwrap();
    		for i in 0..data.len() {
    			if i == data.len()-1 {
    				write!(output, "{}", data[i]).unwrap();
    			} else {
    				write!(output, "{} + ", data[i]).unwrap();
    			}
    		}
    	} else {
    		write!(output, "{n} is NOT perfect.");
    	}
		println!("{output}");
    }

	Ok(())
}