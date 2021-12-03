use std::env;
use std::vec::Vec;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut width: i32 = 0;

    if let Ok(lines) = read_lines(&args[1])
    {
        for line in lines
        {
            if let Ok(mut l) = line {
                if width == 0 {
                    width = l.chars().count() as i32;
                }
                println!("{}", l);
                println!("{:?}", l.pop());
                println!("{}", l.chars().nth(0).unwrap());
            }
        }
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
