// Get DOM Elements
const modal = document.querySelector('#my-modal');
const modalBtnPNL = document.querySelector('#modal-pnl');
const modalBtnReiki= document.querySelector('#modal-reiki');
const modalBtnLaughTherapy = document.querySelector('#modal-laughTherapy');
const closeBtn = document.querySelector('.close');

// Events
modalBtnPNL.addEventListener('click', openModalPNL);
modalBtnReiki.addEventListener('click', openModalReiki);
modalBtnLaughTherapy.addEventListener('click', openModalLaughTherapy);
closeBtn.addEventListener('click', closeModal);
window.addEventListener('click', outsideClick);


// Open
function openModalPNL() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de coach PNL');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Coach PNL');
}

function openModalReiki() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de sistema Reiki');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Sistema Reiki');
}

function openModalLaughTherapy() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de risaterapia');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Certificación Risoterapia');
}


// Close
function closeModal() {
  modal.style.display = 'none';
}

// Close If Outside Click
function outsideClick(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}
