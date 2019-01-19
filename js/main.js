var time = new Date();
var currentTime = "Last Sync: " + time.getDate() + "/"
+ (time.getMonth()+1)  + "/" 
+ time.getFullYear() + " @ "  
+ time.getHours() + ":"  
+ time.getMinutes() + ":" 
+ time.getSeconds();

console.log(currentTime);