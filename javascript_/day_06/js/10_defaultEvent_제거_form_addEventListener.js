const formEl = document.getElementById("my-form");
const nameEl = document.getElementById("name");
const passEl = document.getElementById("pass");
const passCheckEl = document.getElementById("pass-check");

function formSubmitHandler(event) {
  if (!nameEl.value.trim()) {
    alert("이름을 입력하세요");
    nameEl.focus();
    event.preventDefault();
  } else if (!passEl.value.trim()) {
    alert("비밀번호를 입력하세요");
    passEl.focus();
    event.preventDefault();
  } else if (!passCheckEl.value.trim()) {
    alert("비밀번호 확인을 입력하세요");
    passCheckEl.focus();
    event.preventDefault();
  } else if (passEl.value !== passCheckEl.value) {
    alert("비밀번호가 다릅니다. 다시 입력해주세요");
    passEl.value = "";
    passCheckEl.value = "";
    passEl.focus();
    event.preventDefault();
  } else {
    alert("성공");
  }
}

formEl.addEventListener("submit", formSubmitHandler);