/** ex0220_all.js */

// id명을 한글 문자열에 대응 시켜주는 객체
const idToHangul = {
  id: "ID",
  jumin1: "주민번호 앞자리",
  jumin2: "주민번호 뒷자리",
  email: "이메일 주소",
  domain: "이메일 도메인",
  post1: "우편번호",
  address: "주소",
  intro: "자기소개",
};

function validate(id, e, len) {
  const el = document.getElementById(id);
  const v = el.value.trim();
  const isInvalid = !v || (len !== undefined && v.length !== len);

  // 유효하지 않으면 실행 후 true 리턴
  if (isInvalid) {
    e.preventDefault();
    alert(`${idToHangul[id]}이(가) 유효하지 않습니다 다시 입력해주세요.`);
    if (len !== undefined) {
      el.value = "";
    }
    el.focus();
  }
  return isInvalid;
} // validate() end

function check(e) {
  if (validate("id", e)) return;
  if (validate("jumin1", e, 6)) return;
  if (validate("jumin2", e, 7)) return;
  if (validate("email", e)) return;
  if (validate("domain", e)) return;
  if (!document.querySelector("input[name=gender]:checked")) {
    alert("남녀 중 필수로 선택 바랍니다.");
    e.preventDefault();
    return;
  }
  let cnt = document.querySelectorAll("input[name=hobby]:checked").length;
  if (cnt < 2) {
    e.preventDefault();
    alert(`취미는 2개 이상 체크하여야 합니다. 현재 ${cnt}개`);
    return;
  }
  if (validate("post1", e)) return;
  if (validate("address", e)) return;
  if (validate("intro", e)) return;
} // check() end

document.getElementById("myform").addEventListener("submit", check);

function idcheck() {
  const id = document.querySelector("#id");
  const v = id.value.trim();
  if (!v) {
    alert("ID를 입력하세요");
    id.value = "";
    id.focus();
    return;
  }
  const ref = `idcheck.html?id=${v}`; 
  window.open(
    ref, "_blank", "width=300, height=250");
} // idcheck() end

document.getElementById("doubleCheck").addEventListener("click", idcheck);

function move() {
  const jumin1 = document.getElementById("jumin1");
  const jumin2 = document.getElementById("jumin2");

  const pattern1 = /^\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$/;
  if (jumin1.value.length === 6) {
    if (pattern1.test(jumin1.value)) {
      jumin2.focus();
    } else {
      alert("YYMMDD 형식으로 입력하세요");
      jumin1.value = "";
      jumin1.focus();
    }
  }

  const pattern2 = /^[1-4]\d{6}$/;
  if (jumin2.value.length === 7) {
    if (!pattern2.test(jumin2.value)) {
      alert("숫자를 입력하세요");
      jumin2.value = "";
      jumin2.focus();
    } else {
      const male = document.getElementById("gender1");
      const female = document.getElementById("gender2");
      (jumin2.value[0] % 2 ? male : female).checked = true;

      // 윤호형 코드
      // document.getElementById(`gender${2 - (Number(jumin2.value[0]) % 2)}`).checked = true;

      // 초기 구현
      // const genders = document.querySelectorAll("input[name=gender]");
      // genders[jumin2.value[0] % 2 ? 0 : 1].checked = true;
    }
  }
} // move() end

document.getElementById("jumin1").addEventListener("keyup", move);
document.getElementById("jumin2").addEventListener("keyup", move);

function domain1() {
  const domain = document.querySelector("#domain");
  if (!this.value) {
    domain.value = "";
    domain.readOnly = false;
    domain.focus();
  } else {
    domain.value = this.value;
    domain.readOnly = true;
  }
} // domain1() end

document.getElementById("sel").addEventListener("change", domain1);

function post() {
  window.open("post.html", "post", "width=400, height=500");
} // post() end

document.getElementById("postSearch").addEventListener("click", post);
