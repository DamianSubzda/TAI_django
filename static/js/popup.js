let elTitle = document.getElementById("song-title");
let elMp3_audio = document.getElementById("src-song-audio");


function openForm(nr) {
  elMp3_audio.src = '/musics/' + Mp3[nr-1];
  elMp3_audio.load();
  elTitle.innerHTML = Title[nr-1];
  document.getElementById("myForm").style.display = "flex";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
  elMp3_audio.pause();
  elMp3_audio.currentTime = 0;
}

function showInfo(){

}