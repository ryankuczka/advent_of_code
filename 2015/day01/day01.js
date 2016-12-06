var fs = require('fs');

function part1(input) {
    return input.split('(').length - input.split(')').length
};

function part2(input) {
    var floor = 0;
    for (var i = 0; i < input.length; i++) {
        if (input[i] === '(') floor++;
        else floor--;
        // 1-indexed
        if (floor === -1) return i + 1;
    }
};

fs.readFile('./day01/input.txt', 'utf8', function(err, data) {
    if (err) throw err;
    console.log('PART 1', part1(data));
    console.log('PART 2', part2(data));
});
