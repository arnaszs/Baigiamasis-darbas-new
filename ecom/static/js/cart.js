var updateButton = document.getElementsByClassName('update-cart')

for(var i=0; i<updateButton.length; i++){
    updateButton[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        console.log('producId', productId,'action',action)

        console.log('USER',user)

        if(user === 'AnonymousUser'){
            console.log('Not Loged in')
        }
        else{
            updateUserOrder(productId,action)
        }
    })
}


function updateUserOrder(id,act){
    console.log('USER loged in sending data')

    var url = '/update_item/'

    fetch(url,{
        method : 'POST',
        header:{
            'Accept':'application/json',
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': id, 
        'action': act}),
    })

    .then((response) =>{
        return response.json()
    })

    .then ((data)=>
        console.log('data:',data),
        location.reload()
    )

}