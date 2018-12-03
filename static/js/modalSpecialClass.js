// Get DOM Elements
const modal = document.querySelector('#my-modal');
const modalBtnCinemaForum = document.querySelector('#modal-cinemaForum');
const modalBtnConversations= document.querySelector('#modal-conversations');
const modalBtnConferences = document.querySelector('#modal-conferences');
const modalBtnGroup = document.querySelector('#modal-group');
const modalBtnFreeDance = document.querySelector('#modal-freeDance');
const modalBtnKanoi = document.querySelector('#modal-kanoi');
const modalBtnMandala = document.querySelector('#modal-mandala');
const closeBtn = document.querySelector('.close');

// Events
modalBtnCinemaForum.addEventListener('click', openModalCinemaForum);
modalBtnConversations.addEventListener('click', openModalConversations);
modalBtnConferences.addEventListener('click', openModalConferences);
modalBtnGroup.addEventListener('click', openModalGroup);
modalBtnFreeDance.addEventListener('click', openModalFreeDance);
modalBtnKanoi.addEventListener('click', openModalKanoi);
modalBtnMandala.addEventListener('click', openModalMandala);
closeBtn.addEventListener('click', closeModal);
window.addEventListener('click', outsideClick);

// Open
function openModalCinemaForum() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de cine foro');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('cine foro');
}

function openModalConversations() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de conversatorios');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('conversatorios');
}

function openModalConferences() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de conferencias');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('conferencias');
}

function openModalGroup() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de grupos de encuentro');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('grupos de encuentro');
}

function openModalFreeDance() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de baile libre');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('baile libre');
}

function openModalKanoi() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de kanoi');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('Kanoi Movimiento');
}

function openModalMandala() {
  modal.style.display = 'block';
  $("#description").text('Descripción del curso de mándala');
  $("#profesor").text('Profesor: Pedro Pérez');
  $("#modalTitle").text('mándala');
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
