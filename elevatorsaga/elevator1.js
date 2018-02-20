{
    init: function(elevators, floors) {

        var direction = 1;

        function goToFloor(elevator, floorNum) {
            if (floorNum == elevator.currentFloor())
                return;

            if (floorNum > elevator.currentFloor()) {
                //elevator.goingUpIndicator(true);
                //elevator.goingDownIndicator(false);
                direction = 1;
            } else {
                //elevator.goingUpIndicator(false);
                //elevator.goingDownIndicator(true);
                direction = -1;
            }
            elevator.goToFloor(floorNum);
        }

        function changeDirection(elevator) {
            //if (elevator.goingUpIndicator()) {
            if (direction == 1) {
                if (elevator.currentFloor() > 0) {
                    //elevator.goingUpIndicator(false);
                    //elevator.goingDownIndicator(true);
                    direction = -1;
                }
            } else {
                if (elevator.currentFloor() < floors.length - 1) {
                    //elevator.goingUpIndicator(true);
                    //elevator.goingDownIndicator(false);
                    direction = 1;
                }
            }
        }

        function nextFloorCurrentDirection(elevator) {
            // dir = elevator.goingUpIndicator() ? 1 : -1;
            dir = direction;
            for (f = elevator.currentFloor() + dir; f >= 0 && f < floors.length; f += dir)
                if (elevator.getPressedFloors().indexOf(f) != -1)
                    return f;
            return elevator.currentFloor();
        }

        function whenFloorButtonPressed (elevator, floorNum) {
            elevator.goToFloor(floorNum);
            updateDestination(elevator);
        }

        function updateDestination (elevator) {
            if (direction == 1) {
                if (Math.max(...elevator.getPressedFloors()) <= elevator.currentFloor())
                    direction = -1;
            } else {
                if (Math.min(...elevator.getPressedFloors()) >= elevator.currentFloor())
                    direction = 1;
            }
            next_floors = elevator.getPressedFloors().sort();
            curr_floor = elevator.currentFloor();
            if (direction == 1) {
                next_floors = next_floors.filter(i => i > curr_floor).concat(next_floors.filter(i => i <= curr_floor))
            } else {
                next_floors = next_floors.reverse();
                next_floors = next_floors.filter(i => i < curr_floor).concat(next_floors.filter(i => i >= curr_floor))
            }
            elevator.destinationQueue = next_floors;
            elevator.checkDestinationQueue();
        }

        function whenIdle(elevator) {
            //if ((!elevator.goingUpIndicator()) && (!elevator.goingDownIndicator()))
            //    elevator.goingUpIndicator(true);
            f = nextFloorCurrentDirection(elevator);
            if (f != elevator.currentFloor())
                goToFloor(elevator, f);
            else {
                changeDirection(elevator);
                f = nextFloorCurrentDirection(elevator);
                if (f != elevator.currentFloor())
                    goToFloor(elevator, f);
                else {
                    //elevator.goingUpIndicator(false);
                    //elevator.goingUpIndicator(false);
                    //elevator.goingUpIndicator(true);
                    //elevator.goingDownIndicator(true);
                }
            }
        }

        function liftCalled() {
            //for (e = 0; e < elevators.length; e++)
            //    respond(elevators[e]);
        }

        function whenPassingFloor(elevator, floorNum) {
            if (elevator.getPressedFloors().indexOf(floorNum) != -1)
                elevator.goToFloor(floorNum, true);
        }

        for (e = 0; e < elevators.length; e++) {
            elevators[e].on("idle", function() {
                //whenIdle(this);
            });
            elevators[e].on("floor_button_pressed", function(floorNum) {
                whenFloorButtonPressed(this, floorNum);
            });
            elevators[e].on("passing_floor ", function(floorNum, direction) {
                whenPassingFloor(this, floorNum);
            });
        }

        for (f = 0; f < floors.length; f++) {
            floors[f].on("up_button_pressed", function() {
                liftCalled();
            });
            floors[f].on("down_button_pressed", function() {
                liftCalled();
            });
        }
    },

    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}
