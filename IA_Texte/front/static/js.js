console.log("TEST")


document.getElementById('validate').addEventListener('click',function() {
    // Récupérez la valeur du commentaire depuis un champ de texte
    var comment = $('#comment_field').val();
    const api_url = this.getAttribute('data-api-url');
    // Envoyez une requête AJAX vers votre vue Django
    $.ajax({
        url: api_url,  
        method: 'GET',  
        data: {
            comment: comment 
        },
        success: function(response) {
            displayResponse(response['result']);
        },
        error: function(error) {
            console.log('Erreur:', error);
        }
    });
});


function displayResponse(response){
    console.log(response)
    let html;
    if(response.length > 0){
        html = 'Resultat d\'analyse : \n';
        response.forEach((test)=>{
            html += '<p style="color:red">'+test["label"] + ' : '+ test['result'] +'</p>';
            console.log(test);
        })
    }else{
        html = '<p style="color:green">Commentaire valide</p>';
    }
    $('#validation').html(html);
}

