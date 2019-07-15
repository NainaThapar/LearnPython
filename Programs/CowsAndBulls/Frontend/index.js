var chance = 1;
var cnum = 0;
var cow;
var bull;

function showGame() {
  var el = document.getElementsByClassName("game");
  el[0].style.display = "block";
  //console.log(el);
}

function sumitNum() {
  var cowElmnt = "";
  var bullElmnt = "";
  var val = document.getElementById("num-input").value;
  console.log(val);
  fetch(
    "http://localhost:5000/getcowbull?number=" +
      val +
      "&chance=" +
      chance +
      "&chknum=" +
      cnum
  )
    .then(response => {
      return response.json();
    })
    .then(text => {
      if (text.msg) {
        console.log(text.msg);
        alert(text.msg);
      } else {
        cnum = text.num;
        chance = text.chance + 1;
        cow = text.cows;
        bull = text.bulls;
        console.log(text);
        console.log(chance);
        console.log(cnum);
        console.log(cow);
        console.log(bull);
        for (var i = 0; i < cow; i++) {
          cowElmnt +=
            '<img src="./images/cow1.png" width="50px" height="50px" class="cow"/>';
        }
        for (var j = 0; j < bull; j++) {
          bullElmnt +=
            '<img src="./images/bull1.png" width="50px" height="50px" class="bull" />';
        }
        document.getElementById(
          "result-container"
        ).innerHTML += `<div class="result">
            <div class="lbl">Turn ${chance - 1}
          </div>
          <div class="num">
            ${val} 
          </div>
          <div class='img-container'>
            ${cowElmnt} 
            ${bullElmnt} 
          </div>
          </div>`;
      }
    });

  //adding html for the turn to display cows and bulls
  //var resContainer = document.getElementById('result-container').innerHTML;
}
