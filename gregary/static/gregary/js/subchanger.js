(function(){
  var sub_categoryOptions = {"split_a_meal":["Pizza","Paneer","Coming soon"], "video_games":["Fifa","CS","COD"], "sports":["Cricket","Volleyball","Chess"]};
  var category = document.getElementById('category');
  var sub_category = document.getElementById('sub_category');
  //on change is a good event for this because you are guarenteed the value is different
  category.onchange = function(){
      //clear out sub_category
      sub_category.length = 0;
      //get the selected value from category
      var _val = this.options[this.selectedIndex].value;
      //loop through sub_categoryOption at the selected value
      for ( var i in sub_categoryOptions[_val]){
          //create option tag
          var op = document.createElement('option');
          //set its value
          op.value = sub_categoryOptions[_val][i].toLowerCase();
          //set the display label
          op.text = sub_categoryOptions[_val][i];
          //append it to sub_category
          sub_category.appendChild(op);
      }
  };
  //fire this to update sub_category on load
  category.onchange();
})();
