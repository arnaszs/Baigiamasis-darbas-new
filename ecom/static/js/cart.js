const updateUrl = "/update_item/";

const getToken = name => {
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        const cookie = cookies.filter(c => c.trim().substring(0, name.length + 1) === name + '=')[0];
        return decodeURIComponent(cookie.substring(name.length + 1));
    }
    return null;
};

const updateUserOrder = (id, act) => {
    fetch(updateUrl, {
        method: 'POST',
        header: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getToken('csrftoken'),
        },
        body: JSON.stringify({
            'productId': id,
            'action': act
        }),
    }).then(() => {
        window.location.reload();
    });
};