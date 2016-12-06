var fs = require('fs');

function part1(input) {
    var area = 0;

    input.split('\n').forEach(function(line) {
        var lengths = line.split('x').map(x => +x);
        if (lengths.length !== 3) return;
        var sides = [
            lengths[0] * lengths[1],
            lengths[1] * lengths[2],
            lengths[2] * lengths[0]
        ];
        sides.forEach(function(side){area += 2 * side;});
        area += Math.min.apply(Math, sides);
    });
    return area;
}

function part2(input) {
    var ribbon = 0;

    // Go through line by line
    input.split('\n').forEach(function(line) {
        // Get sorted side lengths
        var lengths = line.split('x').map(x => +x).sort((x, y) => x - y);
        if (lengths.length !== 3) return;
        ribbon += 2 * lengths[0] + 2 * lengths[1];
        ribbon += lengths.reduce((pv, cv) => pv * cv);
    });
    return ribbon;
}

fs.readFile('./day02/input.txt', 'utf8', function(err, data) {
    if (err) throw err;
    console.log('PART 1', part1(data));
    console.log('PART 2', part2(data));
});
