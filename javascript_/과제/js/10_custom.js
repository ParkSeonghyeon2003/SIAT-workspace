const formEl = document.getElementById("my-form");
const nameEl = document.getElementById("name");
const passEl = document.getElementById("pass");
const passCheckEl = document.getElementById("pass-check");


function formSubmitHandler(event) {
  const name = nameEl.value.trim();
  const pass = passEl.value.trim();
  const passCheck = passCheckEl.value.trim();
  function check(msg, ...elements) {
    alert(msg);
    elements.forEach(e => e.value = "");
    elements[0].focus();
    event.preventDefault();
  }
  
  if (!name) {
    return check("이름을 입력하세요", nameEl);
  }
  if (!pass) {
    return check("비밀번호를 입력하세요", passEl);
  }
  if (!passCheck) {
    return check("비밀번호 확인을 입력하세요", passCheckEl);
  }
  if (pass !== passCheck) {
    return check("비밀번호가 다릅니다. 다시 입력해주세요.", passEl, passCheckEl);
  }

  alert("성공");
}

formEl.addEventListener("submit", formSubmitHandler);