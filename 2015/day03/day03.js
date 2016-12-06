var fs = require('fs');

var movements = {
    '^': function(pos){return [pos[0], pos[1] + 1];},
    '>': function(pos){return [pos[0] + 1, pos[1]];},
    'v': function(pos){return [pos[0], pos[1] - 1];},
    '<': function(pos){return [pos[0] - 1, pos[1]];}
};

function part1(input) {
    var houses = new Set(),
        position = [0, 0];

    houses.add(position.join(','));

    input.split('').forEach(function(dir) {
        position = movements[dir](position);
        houses.add(position.join(','));
    });

    return houses.size;
}

function part2(input) {
    var houses = new Set(),
        santa_position = [0, 0],
        robo_position = [0, 0];

    houses.add(santa_position.join(','));

    input.split('').forEach(function(dir, i) {
        if (i % 2 === 0) {
            santa_position = movements[dir](santa_position);
            houses.add(santa_position.join(','));
        } else {
            robo_position = movements[dir](robo_position);
            houses.add(robo_position.join(','));
        }
    });

    return houses.size;
}

fs.readFile('./day03/input.txt', 'utf8', function(err, data) {
    if (err) throw err;
    console.log('PART 1', part1(data));
    console.log('PART 2', part2(data));
});
