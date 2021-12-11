let text = `All's well that ends well.
Bad news travels fast.
Well begun is half done.
Birds of a feather  flock together.`

let freqs = {}

for (let i=0; i<text.length;i++){
    let letter = text[i]
    if (freqs[letter]){
        freqs[letter]++
    } else {
        freqs[letter] = 1
    }
}
console.log(freqs)