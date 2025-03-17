var count = 0;
document.getElementById("myButton").onclick = function(){
    count++
    if (count % 2 == 0){
        document.getElementById("demo").innerHTML = "";
    } else {
        var img = document.createElement("img");
        img.src = "https://cs7.pikabu.ru/post_img/2017/12/11/8/1512996545160122863.jpg"
        document.getElementById("demo").appendChild(img);
    }
    
}
