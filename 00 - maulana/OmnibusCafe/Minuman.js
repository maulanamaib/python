function filter()
    {
        if (document.getElementById("Coffee").checked == true)
      {
        a = document.getElementById("coffee1").style.display = 'flex';
        b = document.getElementById("coffee2").style.display = 'flex';
        c = document.getElementById("coffee3").style.display = 'flex';
        d = document.getElementById("noncoffee").style.display = 'none';

      }
      else if (document.getElementById("Non").checked == true)
      {
        a = document.getElementById("coffee1").style.display = 'none';
        b = document.getElementById("coffee2").style.display = 'none';
        c = document.getElementById("coffee3").style.display = 'none';
        d = document.getElementById("noncoffee").style.display = 'flex';
      }
      else
      {
        a = document.getElementById("coffee1").style.display = 'flex';
        b = document.getElementById("coffee2").style.display = 'flex';
        c = document.getElementById("coffee3").style.display = 'flex';
        d = document.getElementById("noncoffee").style.display = 'flex';
      }
    }