document.addEventListener("DOMContentLoaded", function(){
    // check if pay-btn is clicked and then load data to payment page
    document.getElementById("pay-btn").addEventListener("click", function(){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://localhost:8080/esite/cart/getCartData", true);
        xhr.onload = function(){
            if(this.status == 200){
                var data = JSON.parse(this.responseText);
                var total = 0;
                var html = "";
                for(var i = 0; i < data.length; i++){
                    total += data[i].price * data[i].quantity;
                    html += "<tr><td>" + data[i].name + "</td><td>" + data[i].price + "</td><td>" + data[i].quantity + "</td><td>" + data[i].price * data[i].quantity + "</td></tr>";
                }
                document.getElementById("cart-table").innerHTML = html;
                document.getElementById("total").innerHTML = total;
            }
        }
        xhr.send();
    });
});


