### How to dynamically create table in Twig

```
<table class="table table-bordered">
    <thead>
        <tr>
            {% for range, dets in rents %}
                <th scope="col">{{range}}</th>
            {% endfor %}
        </tr>
    </thead>
    <tbody>
        <tr>
            {% for range, details in rents %}
                <td scope="row">{{details.item}}</td>
            {% endfor %}
        </tr>
    </tbody>
</table>
```