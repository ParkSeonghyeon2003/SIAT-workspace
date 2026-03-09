const formEl = document.getElementById("my-form");
const nameEl = document.getElementById("name");
const passEl = document.getElementById("pass");
const passCheckEl = document.getElementById("pass-check");

/*
  내부 함수는 최대한 지양한다.
  함수가 매번 생성 및 삭제되는 것이 바람직 하지 않다.
*/
function handleError(event, msg, ...els) {
  event.preventDefault();
  alert(msg);
  els.forEach(e => e.value = "");
  els[0].focus();
}

function formSubmitHandler(event) {
  const name = nameEl.value.trim();
  const pass = passEl.value.trim();
  const passCheck = passCheckEl.value.trim();
  
  // 유효성 검사
  if (!name) {
    return handleError(event, "이름을 입력하세요", nameEl);
  }
  if (!pass) {
    return handleError(event, "비밀번호를 입력하세요", passEl);
  }
  if (!passCheck) {
    return handleError(event, "비밀번호 확인을 입력하세요", passCheckEl);
  }
  if (pass !== passCheck) {
    return handleError(event, "비밀번호가 다릅니다. 다시 입력해주세요.", passEl, passCheckEl);
  }

  alert("성공");
}

formEl.addEventListener("submit", formSubmitHandler);