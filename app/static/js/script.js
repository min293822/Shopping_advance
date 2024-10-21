let cartBtns = document.querySelectorAll('.cartbtn');
itemOut = document.getElementById('cart');

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {1
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

cartBtns.forEach(btn =>{
  btn.addEventListener('click', addToCart)
});

function addToCart(e){
  let product_id = e.target.value;
  let url = "add_cart/";
  let data = {id:product_id}

  fetch(url, {
    method:'POST',
    headers:{
      "Content-Type": "application/json", 
      "X-CSRFToken": csrftoken},
    body: JSON.stringify(data)
  }).then(res=>res.json()).then(data=>{
    itemOut.innerHTML = data;
    console.log(data);
  }).catch(error=>{
    console.log(error);
  });
  
  
}


