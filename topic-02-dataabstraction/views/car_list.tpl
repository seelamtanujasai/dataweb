<html>
<body>
<h2> List of Cars </h2>
<hr/>
<table>
% for item in car_list:
 <tr>
<td> {{str(item['desc'])}} </td>
<td> <a href="/edit/{{str(item['id'])}}">Edit</a> </td>
<td> <a href="/delete/{{str(item['id'])}}">Delete</a> </td>
 </tr>
% end
</table>
<hr/>
<form action = "/add" method ="post">
   <p> Add new Car : <input name = "description"/></p>
   <p><button type ="submit"> Submit </button>
</form>
</body>
</html>