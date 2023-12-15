const popupLinks = document.querySelectorAll(".popup-link"),
    body = document.querySelector("body"),
    lockPadding = document.querySelectorAll(".lock-padding");
let unlock = !0;
const timeout = 400;
if (popupLinks.length > 0)
    for (let e = 0; e < popupLinks.length; e++) {
        const t = popupLinks[e];
        t.addEventListener("click", (function(e) {
            const o = t.getAttribute("href").replace("#", "");
            popupOpen(document.getElementById(o)), e.preventDefault()
        }))
    }
const popupCloseIcon = document.querySelectorAll(".close-popup");
if (popupCloseIcon.length > 0)
    for (let e = 0; e < popupCloseIcon.length; e++) {
        const t = popupCloseIcon[e];
        t.addEventListener("click", (function(e) {
            popupClose(t.closest(".popup")), e.preventDefault()
        }))
    }

function popupOpen(e) {
    if (e && unlock) {
        const t = document.querySelector(".popup.open");
        t ? popupClose(t, !1) : bodyLock(), e.classList.add("open"), e.addEventListener("mousedown", (function(e) {
            e.target.closest(".popup__content") || popupClose(e.target.closest(".popup"))
        }))
    }
}

function popupClose(e, t = !0) {
    unlock && (e.classList.remove("open"), e.classList.contains("_complete") && setTimeout((function() {
        e.classList.remove("_complete")
    }), 400), t && bodyUnlock())
}

function bodyLock() {
    const e = window.innerWidth - document.querySelector(".wrapper").offsetWidth + "px";
    for (let t = 0; t < lockPadding.length; t++) {
        lockPadding[t].style.paddingRight = e
    }
    body.style.paddingRight = e, body.classList.add("lock"), unlock = !1, setTimeout((function() {
        unlock = !0
    }), 400)
}

function bodyUnlock() {
    setTimeout((function() {
        if (lockPadding.length > 0)
            for (let e = 0; e < lockPadding.length; e++) {
                lockPadding[e].style.paddingRight = "0px"
            }
        body.style.paddingRight = "0px", body.classList.remove("lock")
    }), 400), unlock = !1, setTimeout((function() {
        unlock = !0
    }), 400)
}
document.addEventListener("keydown", (function(e) {
    if (27 == e.which) {
        popupClose(document.querySelector(".popup.open"))
    }
}));
let cart_items_count = 0,
    total_price = 0,
    cart_items = {};
const cart = document.querySelector(".cart__body"),
    cart_counter = document.querySelector(".cart__counter"),
    cart_total_price = document.querySelector(".cart__total_price");
let stored = JSON.parse(localStorage.getItem("cart_items"));

function get_localStorage() {
    let e = new FormData;
    e.append("cart", JSON.stringify(stored)), fetch("api/cart", {
        method: "post",
        body: e
    }).then((function(e) {
        return e.json()
    })).then((function(e) {
        for (const [t, o] of Object.entries(e)) add_item_to_cart(t, o.count, {
            title: o.name,
            weight: o.weight,
            price: o.price,
            image: o.photo_url
        }), cart_items[t] = {
            price: o.price,
            count: o.count
        }, cart_items_count += Number(o.count), total_price += Number(o.count) * Number(o.price);
        change_cart()
    }))
}

function change_cart() {
    cart_counter.innerHTML = cart_items_count, cart_total_price.innerHTML = total_price + "₽", document.querySelector(".cart__delivery").style.display = total_price > 599 ? "block" : "none", 0 === cart_items_count ? cart.classList.contains("_empty") || cart.classList.add("_empty") : cart.classList.contains("_empty") && cart.classList.remove("_empty")
}

function cleaning_the_cart() {
    localStorage.clear(), cart_items_count = 0, total_price = 0, cart_items = {}, stored = {}, change_cart();
    document.querySelectorAll(".cart__item").forEach((e => {
        e.classList.contains("cart__item_template") || (console.log(e), e.parentNode.removeChild(e))
    }))
}

function add_item_to_cart(e, t, o) {
    const c = document.querySelector(".cart__items"),
        r = document.querySelector(".cart__item_template").cloneNode(!0);
    r.classList.remove("cart__item_template"), r.setAttribute("data-id", e), r.querySelector(".counter__value").innerHTML = t, r.querySelector(".cart__item-title").innerHTML = o.title, r.querySelector(".cart__item-weight").innerHTML = o.weight, r.querySelector(".cart__item-price").innerHTML = o.price, r.querySelector(".cart__item-image").src = o.image, c.appendChild(r)
}
stored || (localStorage.setItem("cart_items", JSON.stringify({})), stored = {}), Object.keys(stored).length > 0 ? get_localStorage() : change_cart();
const items = document.querySelector(".home__items");
items.addEventListener("click", (function(e) {
    if (e.target.closest(".counter__button_del") || e.target.closest(".counter__button_add")) {
        const t = e.target.closest(".counter").querySelector(".counter__value"),
            o = e.target.closest(".popup__footer").querySelector(".popup__price");
        let c = Number(t.textContent);
        const r = Number(o.innerHTML.replace("₽", "")) / c;
        e.target.closest(".counter__button_del") ? c > 1 && (t.innerHTML = c - 1, o.innerHTML = Number(o.innerHTML.replace("₽", "")) - r + "₽") : e.target.closest(".counter__button_add") && (t.innerHTML = c + 1, o.innerHTML = Number(o.innerHTML.replace("₽", "")) + r + "₽")
    }
    if (e.target.closest(".popup__button")) {
        const t = e.target.closest(".popup__buttons-wrapper").querySelector(".counter").querySelector(".counter__value");
        let o = Number(t.textContent);
        const c = e.target.closest(".popup"),
            r = c.getAttribute("data-id");
        if (r in cart_items) {
            cart_items_count += o, total_price += cart_items[r].price * o, cart_items[r].count += o;
            document.querySelector(".cart__items").querySelector(`[data-id="${r}"]`).querySelector(".counter__value").innerHTML = cart_items[r].count, c.querySelector(".popup__price").innerHTML = cart_items[r].price + "₽", document.querySelector(".cart__delivery").style.display = total_price > 599 ? "block" : "none"
        } else {
            let e = Number(c.closest(".home__item").querySelector(".home__item-price").innerHTML.replace("₽", ""));
            cart_items[r] = {
                count: o,
                price: e
            }, c.querySelector(".popup__price").innerHTML = cart_items[r].price + "₽", add_item_to_cart(r, o, {
                title: c.querySelector(".popup__title").innerHTML,
                weight: c.querySelector(".popup__weight").innerHTML.split(",")[0],
                price: c.querySelector(".popup__price").innerHTML,
                image: c.querySelector(".popup__image").src,
                count: c.querySelector(".counter__value").innerHTML = o
            }), cart_items_count += o, total_price += o * e
        }
        t.innerHTML = 1, stored[r] = cart_items[r].count, localStorage.setItem("cart_items", JSON.stringify(stored)), change_cart()
    }
}));
const cart_items_node = document.querySelector(".cart__items");
cart_items_node.addEventListener("click", (function(e) {
    if (e.target.closest(".counter__button_del") || e.target.closest(".counter__button_add")) {
        const t = e.target.closest(".counter").querySelector(".counter__value"),
            o = e.target.closest(".cart__item"),
            c = o.getAttribute("data-id");
        let r = Number(t.textContent);
        e.target.closest(".counter__button_del") ? (r > 1 && (t.innerHTML = r - 1, cart_items_count -= 1, total_price -= cart_items[c].price, cart_items[c].count -= 1, stored[c] -= 1), 1 === r && (cart_items_count -= 1, total_price -= cart_items[c].price, delete cart_items[c], delete stored[c], cart_items_node.removeChild(o), change_cart())) : e.target.closest(".counter__button_add") && (t.innerHTML = r + 1, cart_items_count += 1, total_price += cart_items[c].price, cart_items[c].count += 1, stored[c] += 1), localStorage.setItem("cart_items", JSON.stringify(stored)), document.querySelector(".cart__delivery").style.display = total_price > 599 ? "block" : "none", cart_total_price.innerHTML = total_price + "₽", cart_counter.innerHTML = cart_items_count
    }
}));
const delivery_popup = document.querySelector(".popup__delivery").querySelector(".popup__content");
if (delivery_popup) {
    const e = delivery_popup.querySelector(".popup__form"),
        t = delivery_popup.querySelectorAll('input[type="text"], input[type="tel"]');
    delivery_popup.addEventListener("click", (function(t) {
        t.target.closest('input[id="delivery"]') && (e.classList.remove("_pickup"), e.classList.add("_delivery")), t.target.closest('input[id="pickup"]') && (e.classList.remove("_delivery"), e.classList.add("_pickup"))
    })), e.addEventListener("submit", (o => {
        o.preventDefault();
        const c = delivery_popup.querySelector('input[id="pickup"]').checked;
        validate_form(t, c) && submit_form(e, t)
    }))
}

function submit_form(e, t) {
    e.closest(".popup__delivery").classList.add("_load");
    const o = e.action,
        c = document.querySelector(".popup__result_desc");
    let r = new FormData(e),
        n = {};
    for (const [e, t] of Object.entries(cart_items)) n[e] = t.count;
    r.append("products", JSON.stringify(n)), fetch(o, {
        method: "post",
        headers: {
            "X-CSRFToken": String(r.get("csrfmiddlewaretoken"))
        },
        body: r
    }).then((o => {
        e.closest(".popup__delivery").classList.remove("_load"), 200 === o.status ? (c.textContent = "Ваш заказ успешно принят!", e.closest(".popup__delivery").classList.add("_complete"), t.forEach((e => {
            e.value = ""
        })), cleaning_the_cart()) : (c.textContent = "Что-то пошло не так, попробуйте позже.", e.closest(".popup__delivery").classList.add("_complete"))
    }))
}

function validate_form(e, t) {
    var o = !1;
    return t ? e.forEach((e => {
        "delivery_input_name" === e.id ? "" === e.value ? (e.classList.add("_warning"), o = !0) : e.classList.remove("_warning") : "tel" === e.type && (validate_phone(e.value) ? e.classList.remove("_warning") : (e.classList.add("_warning"), o = !0))
    })) : e.forEach((e => {
        "" === e.value ? (e.classList.add("_warning"), o = !0) : "tel" === e.type ? validate_phone(e.value) ? e.classList.remove("_warning") : (e.classList.add("_warning"), o = !0) : e.classList.remove("_warning")
    })), !o
}

function validate_phone(e) {
    if ((e = e.replace(/\s/g, "")).length >= 11 && e.length <= 12) {
        return /^[0-9\s+]*$/.test(String(e))
    }
    return !1
}
const filter_form = document.querySelector(".home__filter");
if (filter_form) {
    let e = document.getElementById("filter_input");
    const t = new URLSearchParams(window.location.search).get("category");
    let o = document.querySelector('li[data-id="0"]');
    t ? (o = document.querySelector(`li[data-id="${t}"]`), o.classList.add("_active")) : o.classList.add("_active");
    let c = o;
    filter_form.addEventListener("click", (t => {
        t.preventDefault();
        const o = t.target.closest("li");
        o && (o.classList.contains("_active") || (c.classList.remove("_active"), o.classList.add("_active"), c = o, e.value = o.getAttribute("data-id"), filter_form.submit()))
    }))
}