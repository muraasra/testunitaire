from catalog.forms import BookForm

def test_form_valid(author, category):
    form = BookForm(data={
        "title": "I, Robot",
        "author": author.id,
        "category": category.id,
        "isbn": "9780553382563",
        "available_copies": 3,
    })
    assert form.is_valid()