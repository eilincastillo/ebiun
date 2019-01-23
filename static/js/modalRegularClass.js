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
  var obj = $("#description").text('A traves de la practica del Yoga se logra  equilibrio  ' +
      'y armonia del cuerpo, mente y espíritu. Los beneficios del Yoga son innumerables a nivel fisico, mental y espiritual. \n \n' +
      'Beneficios:\n' +
      '\n' +
      'Físicos: ayuda a prevenir enfermedades, fortalece y flexibiliza todo el  cuerpo, estimula el funcionamiento de las glándulas tiroides y paratiroides, ' +
      'desarrollo de la respiración consciente-mayor oxigenación, refuerza el sistema inmunológico y endocrino, proporciona más equilibrio físico, fortalece músculos y cuerpo, ' +
      'ayuda al sistema neuromuscular y las articulaciones, genera estados de relajación que reducen el ritmo cardiaco y la presión sanguínea, proporciona flexibilidad a  la columna vertebral.\n' +
      '\n' +
      'Mentales: disminuye la ansiedad, la depresión, el estrés, ayuda a potenciar la capacidad de concentración y la memoria, aumenta la creatividad, fortalece la autoestima y ' +
      'eleva el nivel de conciencia del individuo de si mismo como del todo del cual forma parte. \n' +
      '\n' +
      'Espirituales: en estos beneficios juega parte muy importante la meditación, la cual representa la esencia espiritual de la práctica del yoga y que nos conduce a la ' +
      'unión perfecta del cuerpo y la mente en uno solo, y nos permite encontrarnos con nuestro propio ser y yo interior, donde verdaderamente se encuentra Dios. ' +
      'El principal beneficio es el estado de conexión consigo mismo.');
  obj.html(obj.html().replace(/\n/g,'<br/>'));
  $("#profesor").text('Duracion de la actividad: 1 hora');
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
  var obj = $("#description").text('La sesión diaria de meditación va dirigida a proporcionar herramientas para que el participante pueda durante y después de la clase encontrar paz y armonía interior, mediante una práctica guiada enfocados en la postura correcta, la respiración, generar un estado de relajación, en la observación de los pensamientos y visualización.\n \n' +
      'La meditación nos proporciona fortalecimiento de nuestro ser espiritual, desarrollo de la conciencia, fortalece la concentración, potencia las habilidades y capacidades, mayor estado de felicidad y plenitud, cambio en la forma de abordar las situaciones y problemas, mayor empatía y fuerza de voluntad.');
  obj.html(obj.html().replace(/\n/g,'<br/>'));
  $("#profesor").text('Duracion de la actividad: 1 hora');
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
