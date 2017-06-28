
/*!
 * Draw Maze
 */

//Get Information About Canvas
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
var width = canvas.width;
var height = canvas.height;
var moveToX = 100;
var moveToY = 100;

//ctx.fillStyle = "#FF0000";
//ctx.fillRect(0,0,150,75);

ctx.fillStyle = "#000000";
//ctx.beginPath();
//ctx.moveTo(100,100);
//ctx.lineTo(95,105);
//ctx.lineTo(105,105);
//ctx.fill();

//ctx.beginPath();
//ctx.moveTo(100,100);
//ctx.lineTo(100,150);
//ctx.lineTo(75,150);
//ctx.lineTo(75,200)
//ctx.stroke();

//ctx.fillRect(50,50,1,1);
//ctx.fillRect(52,52,1,1);

function setRobotLocation(x_coord, y_coord, angle) {
    //code
}

function delayedAlert() {
    //code
    //timeoutID = window.setTimeout(slowAlert, 2000);
    slowAlert();
    
}

function slowAlert() {
    //showConsole("alright, alright, alright");
    numX = Math.floor((Math.random() * 200) + 1);
    numY = Math.floor((Math.random() * 200) + 1);
    ang = Math.floor((Math.random() * 360) + 1);
    showConsole("Selected: " + numX + ", " + numY + "(" + ang + ")")
    //showConsole("coordinates selected: " + numX + ", " + numY)
    
    setImage();
    
    //Draw Triangle to show direction
    ctx.save();
    ctx.moveTo(numX, numY);
    ctx.translate(numX, numY); 
    ctx.rotate(Math.radians(ang)); // Rotate in degrees (in radians)
    //ctx.moveTo(numX, numY);
    ctx.lineTo(-5, 5);
    ctx.lineTo(5, 5);
    ctx.fill();
    ctx.restore();
    
    ctx.beginPath();
    ctx.moveTo(moveToX,moveToY);
    ctx.lineTo(numX,numY);
    ctx.stroke();
    
    
    //ctx.moveTo(100,100);
    //ctx.lineTo(95,105);
    //ctx.lineTo(105,105);
    //ctx.fill();
    
    
    
    moveToX = numX;
    moveToY = numY;
    
}

// Converts from degrees to radians.
Math.radians = function(degrees) {
  return degrees * Math.PI / 180;
};

function clearAlert() {
    //code
    window.clearTimeout(timeoutID);
}

function setImage() {
    //code
    var com = document.getElementById("main_image").src = '/image/bob.png';
}

function showConsole(alerts) {
    //code
    var com = document.getElementById("findings").innerHTML;
    document.getElementById("findings").innerHTML = com + "<p class='p-left'>" + Date() + " " + alerts + "</p>";
    
    var com = document.getElementById("logging").innerHTML;
    document.getElementById("logging").innerHTML = com + "<p class='p-left'>" + Date() + " " + alerts + "</p>";

}