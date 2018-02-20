{
    init: function(elevators, floors) {
        function whenFloorButtonPressed (elevator, floorNum) {
            elevator.goToFloor(floorNum);
            updateDestination(elevator);
        }

        function updateDirection (elevator) {
            pressed_floors = elevator.getPressedFloors();
            if (pressed_floors.length > 0) {
                if (elevator.direction == 1) {
                    if (Math.max(...pressed_floors) > elevator.currentFloor())
                        return -1;
                } else {
                    if (Math.min(...pressed_floors) < elevator.currentFloor())
                        return -1;
                }
            }

            if (elevator.direction == 1)
                curr_floor = Math.ceil(elevator.currentFloor());
            else
                curr_floor = Math.floor(elevator.currentFloor());

            f = curr_floor + elevator.direction;

            for (; f > 0 && f < floors.length - 1; f += elevator.direction) {
                if (elevator.direction == 1) {
                    if (floors[f].up_pressed)
                        return f;
                } else {
                    if (floors[f].down_pressed)
                        return f;
                }
            }

            for (; f >= 0 && f <= floors.length - 1; f -= elevator.direction) {
                if (floors[f].up_pressed || floors[f].down_pressed)
                    return f;
            }

            return -1;
        }

        function updateDestination (elevator) {
            next_floors = elevator.getPressedFloors();

            add_floor = updateDirection(elevator);
            if (add_floor >= 0) {
                next_floors.push(add_floor);
                if (add_floor > elevator.currentFloor())
                    elevator.direction = 1;
                else if (add_floor < elevator.currentFloor())
                    elevator.direction = -1;
            }

            //if (next_floors.length == 0) {
            //}

            next_floors.sort();
            curr_floor = elevator.currentFloor();
            if (elevator.direction == 1) {
                next_floors = next_floors.filter(i => i > curr_floor).concat(next_floors.filter(i => i <= curr_floor))
            } else {
                next_floors = next_floors.reverse();
                next_floors = next_floors.filter(i => i < curr_floor).concat(next_floors.filter(i => i >= curr_floor))
            }
            elevator.destinationQueue = next_floors;
            elevator.checkDestinationQueue();
        }

        function whenPassingFloor(elevator, floorNum) {
            if (elevator.getPressedFloors().indexOf(floorNum) != -1)
                elevator.goToFloor(floorNum, true);
        }

        function whenStoppedAtFloor(elevator, floorNum) {
            if (elevator.direction == 1)
                floors[floorNum].up_pressed = false;
            else
                floors[floorNum].down_pressed = false;
        }

        function updateAllElevators () {
            for (e = 0; e < elevators.length; e++)
                updateDestination(elevators[e]);
        }

        for (f = 0; f < floors.length; f++) {
            floors[f].up_pressed = false;
            floors[f].down_pressed = false;
            floors[f].on("up_button_pressed", function() {
                this.up_pressed = true;
                updateAllElevators();
            });
            floors[f].on("down_button_pressed", function() {
                this.down_pressed = true;
                updateAllElevators();
            });
        }

        for (e = 0; e < elevators.length; e++) {
            elevators[e].direction = 1;
            elevators[e].on("idle", function() {
                updateDestination(this);
            });
            elevators[e].on("floor_button_pressed", function(floorNum) {
                whenFloorButtonPressed(this, floorNum);
            });
            elevators[e].on("passing_floor ", function(floorNum, direction) {
                whenPassingFloor(this, floorNum);
            });
            elevators[e].on("stopped_at_floor ", function(floorNum) {
                whenStoppedAtFloor(this, floorNum);
            });
        }
    },

    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}
