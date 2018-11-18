// Get DOM Elements
const modal = document.querySelector('#my-modal');
const modalBtnYoga = document.querySelector('#modal-yoga');
const modalBtnChikun = document.querySelector('#modal-chikun');
const modalBtnMeditation = document.querySelector('#modal-mediation');
const modalBtnRelax = document.querySelector('#modal-relax');
const modalBtnPranayamas = document.querySelector('#modal-pranayamas');
const modalBtnRehabilitation = document.querySelector('#modal-rehabilitation');
const closeBtn = document.querySelector('.close');

// Events
modalBtnYoga.addEventListener('click', openModalYoga);
modalBtnChikun.addEventListener('click', openModalChikun);
modalBtnMeditation.addEventListener('click', openModalMeditation);
modalBtnRelax.addEventListener('click', openModalRelax);
modalBtnPranayamas.addEventListener('click', openModalPranayamas);
modalBtnRehabilitation.addEventListener('click', openModalRehabilitation);
closeBtn.addEventListener('click', closeModal);
window.addEventListener('click', outsideClick);

// Open
function openModalYoga() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de yoga');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Yoga');
}

function openModalChikun() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de chi kun');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Chi kun');
}

function openModalMeditation() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de meditación');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('meditación');
}

function openModalRelax() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de relajación');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Practicas de relajación');
}

function openModalPranayamas() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de pranayamas');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('pranayamas');
}

function openModalRehabilitation() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de rehabilitación');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Programa de Rehabilitación');
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
