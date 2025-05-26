use std::io;

// 1193: 분수찾기

fn main() {
    let mut x = String::new();
    io::stdin().read_line(&mut x).expect("failed: input");
    let x : usize = x.trim().parse().expect("failed: parse");

    let mut l = 1;
    let mut r;
    let mut temp;
	let mut down: bool = true;
	let mut count = 1;
	
	loop {
		temp = l + 4*count;
		if x < temp {
			r = count;
			count = l;
			l = r;
			if count > 1 {
				down = false;
			}
			break;
		}
		l = temp;
		count += 1;
	}

	for i in 0..(x-count) {
		if l == 1 {
			if r % 2 == 1 {
				r += 1;
			} else {
				down = true;
				r -= 1;
				l += 1;
			}
		} else {
			if r == 1 {
				if l % 2 == 0 {
					l += 1;
				} else {
					down = false;
					l -= 1;
					r += 1;
				}
			} else {
				if down {
					r -= 1;
					l += 1;
				} else {
					l -= 1;
					r += 1;
				}
			}
		}
	}

	println!("{l}/{r}");
}