

$(".btn-insert-data").click(function(){
  var name=$("#ins_name").val();
  if (name==""){
    console.log("name is null")
  }
  else{
    &.ajax({
        url:'{%  url 'staff_add_case' %}',
        type:'POST',
        data:{name:name}
    })
    .done(function(response){
      console.log("response")
    })
    .fail(function(){
      console.log("Error")
    })
  }
})