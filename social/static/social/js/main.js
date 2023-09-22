$(document).ready(function(){

    $(".like-post").on("submit", function(e){
        e.preventDefault()
        const post_id = $(this).attr("id")
        const url = $(this).attr("action")
        
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                'post_id': post_id,
            },
            success: function(response) {
                $(`.like-counter${post_id}`).text(response['likes_count'])
                if(response['liked'] === true) {
                    $(`.like-btn-${post_id}`).children("i").remove()
                    $(`.like-btn-${post_id}`).append('<i class="bi bi-heart-fill"></i>')
                    $(`.like-btn-${post_id}`).toggleClass('text-secondary text-danger');
                } else {
                    $(`.like-btn-${post_id}`).children("i").remove()
                    $(`.like-btn-${post_id}`).append('<i class="bi bi-heart"></i>')
                    $(`.like-btn-${post_id}`).toggleClass('text-danger text-secondary');
                }
            },
        });
    });

    $(".like-comment").on("submit", function(e){
        e.preventDefault()
        const comment_id = $(this).attr("id")
        const url = $(this).attr("action")
        
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                'comment_id': comment_id,
            },
            success: function(response) {
                $(`.like-counter${comment_id}`).text(response['likes_count'])
                if(response['liked'] === true) {
                    $(`.like-btn-${comment_id}`).children("i").remove()
                    $(`.like-btn-${comment_id}`).append('<i class="bi bi-heart-fill"></i>')
                    $(`.like-btn-${comment_id}`).toggleClass('text-secondary text-danger');
                } else {
                    $(`.like-btn-${comment_id}`).children("i").remove()
                    $(`.like-btn-${comment_id}`).append('<i class="bi bi-heart"></i>')
                    $(`.like-btn-${comment_id}`).toggleClass('text-danger text-secondary');
                }
            },
        });
    });
});