const copyBtn = document.querySelector('.copy_btn');

$(function(){
    let url = window.location.href;
    let img = $('.result_img img').attr('src');

    $("meta[property='og\\:url']").attr('content', url);
    $("meta[property='og\\:image']").attr('content', img);
});

function copyUrl(){
    const url = window.location.href;

    navigator.clipboard.writeText(url).then(() => {
        alert("URL이 복사되었습니다"); 
    });
}

copyBtn.addEventListener('click', copyUrl);