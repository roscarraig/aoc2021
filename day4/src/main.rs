use std::env;
use std::vec::Vec;
use std::fs;

struct Card {
    marked: Vec<usize>,
    grid: [[usize; 5]; 5],
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1].to_string();
    let data = fs::read_to_string(filename).expect("Unable to open file");
    let mut blocks = data.split("\n\n");
    // let mut blocks = fs::read_to_string(filename).split("\n\n");
    let calls = blocks.next().unwrap().split(',').map(|n| n.parse().unwrap());
    let mut cards: Vec<Card> = blocks.map(
        |card| card.lines().map(
            |line| line.split_whitespace().map(
                |n| n.parse().ok()
            ).collect()
        ).collect()
    ).collect();

}
