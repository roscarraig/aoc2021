use std::env;
use std::vec::Vec;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

struct Card {
    marked: Vec<u8>,
    grid: [[u8; 5]; 5],
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if let Ok(mut lines) = read_lines(&args[1])
    {
        println!("Hello!");
        let pline = lines.next();
        println!("{:?}", pline.unwrap());
        // let parts = lines.next().unwrap().split(",");
        // let calls = parts.collect::<Vec<&str>>();
        // for item in calls
        // {
        //     println!("{}", item);
        // }
        // println!("=====");
        // for line in lines
        // {
            // println!("{}", line.unwrap());
        // }
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
