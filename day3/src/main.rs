use std::env;
use std::vec::Vec;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut readings: Vec<i32> = Vec::new();
    let mut width: i32 = 0;
    let mut gamma: i32 = 0;
    let mut epsilon: i32 = 0;

    if let Ok(lines) = read_lines(&args[1])
    {
        for line in lines
        {
            let mut num :i32 = 0;
            if let Ok(l) = line {
                if width == 0 {
                    width = l.chars().count() as i32;
                }
                for it in 0..width
                {
                    num *= 2;
                    if l.chars().nth(it as usize).unwrap() == '1' {
                        num += 1;
                    }
                }
            }
            readings.push(num);
        }
    }
    for i in 0..width
    {
        gamma *= 2;
        epsilon *= 2;
        gamma += most(&readings, i, width);
        epsilon += least(&readings, i, width);
    }
    println!("Part 1 {}", gamma * epsilon);
    println!("Part 2 {}", filter(&readings, width, 1) * filter(&readings, width, 0));
}

fn most(v: &Vec<i32>, pos: i32, len: i32) -> i32
{
    let mut ones: i32 = 0;
    let mask = 1 << (len - pos - 1);
    for i in 0..v.len()
    {
        if (mask & v[i]) == mask
        {
            ones += 1;
        }
    }
    if ones * 2 >= v.len() as i32
    {
        return 1;
    }
    return 0;
}

fn least(v: &Vec<i32>, pos: i32, len: i32) -> i32
{
    let mut ones: i32 = 0;
    let mask = 1 << (len - pos - 1);
    for i in 0..v.len()
    {
        if (mask & v[i]) == mask
        {
            ones += 1;
        }
    }
    if ones * 2 < v.len() as i32
    {
        return 1;
    }
    return 0;
}

fn filter(input: &Vec<i32>, width: i32, bit: i32) -> i32
{
    let mut copy = input.clone();
    let mut value :i32 = 0;
    let mut cbit :i32;

    for i in 0..width
    {
        if bit == 1
        {
            cbit = most(&copy, i, width) << (width - i - 1)
        } else {
            cbit = least(&copy, i, width) << (width - i - 1)
        }
        value += cbit;
        copy.retain(|&x| (x & (1 << (width - i - 1))) == cbit);
        if copy.len() == 1
        {
            return copy[0];
        }
    }
    return value;
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
