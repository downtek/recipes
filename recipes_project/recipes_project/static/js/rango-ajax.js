$(document).ready(function(){
    // JQuery code to be added in here.
    $('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/recipes/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
           });
});
    $('#suggestion').keyup(function(){
            var query;
            query = $(this).val();
            $.get('/recipes/suggest_category/', {suggestion: query}, function(data){
                $('#cats').html(data);
            });
    });

    $('.recipes-add').click(function(){
        var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this)
            $.get('/recipes/auto_add_page/', {category_id: catid, url: url, title: title}, function(data){
                $('#pages').html(data);
                me.hide();
            });
    });

});
