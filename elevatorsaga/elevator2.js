{
    init: function(elevators, floors) {

        var direction = 1;

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
                updateDestination(this);
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
