let counter = 0;

document.getElementById('btnR').addEventListener('click', function () {
  const childrens = document.body.childNodes;
  let i = 0;
  for (let children of childrens) {
    console.log(children);
    if (counter === i) {
      children.classList.add('hidden');
    }
    i++;
  }
});
