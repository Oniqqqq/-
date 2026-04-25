import os

path = "/home/dzhalil/Рабочий стол/антигравити/nikamed/artifacts/myhealthprac/static/index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Target is the footer start
target = "<div class=\"footer\">"

# Content to insert BEFORE the footer
insertion = """
<section data-w-id="5aa2be89-4ce8-7ee1-5bdb-26ace158f535" class="fullsize_gradient">
  <div class="gradient_code w-embed w-script">
    <script>
      window.addEventListener("load", function () {
        if (typeof VANTA !== 'undefined') {
          VANTA.FOG({
            el: "#vanta-bg",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            highlightColor: 0xCAB190,
            midtoneColor: 0x874318,
            lowlightColor: 0x170903,
            baseColor: 0x170903,
            blurFactor: 1.0,
            speed: 1.5,
            zoom: 1.1
          });
        }
      });
    </script>
    <style>
      .vanta-wrapper {
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        z-index: 0;
      }
      #vanta-bg {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: auto !important;
        z-index: 0 !important;
      }
      .content_above {
        pointer-events: auto;
      }
    </style>
  </div>
  <div class="background_video gradient">
    <div class="overlay_video"></div>
    <div class="vanta_bg w-embed">
      <div class="vanta-wrapper" style="width:100vw; height:100%;">
        <div id="vanta-bg" style="width:100vw; height:100%;"></div>
      </div>
    </div>
  </div>
  <div class="content_above">
    <div class="headline_gradient">
      <h2 letters-slide-up="" text-split="" class="h2 txt_grd">Единая экосистема ортопедических решений, созданная развиваться вместе с вами</h2>
    </div>
    <div class="cms_list_bullet">
      <div class="w-dyn-list">
        <div role="list" class="list_cms_long w-dyn-items">
          <div role="listitem" class="bullet_item">
            <div class="flexbox_spec">
              <div class="flex_icon">
                <div class="circle_icon"><img src="/images/6825086476a58e031cf28278_minutes-icon.avif" loading="lazy" alt=""/></div>
                <div class="title_pd"><div class="title_cms">За считанные минуты</div></div>
              </div>
              <div class="bullet_list">
                <div><div class="title_cms">Быстрый старт. Точный подбор.</div></div>
                <div class="bullet_cms">
                  <div class="rich_bullet w-richtext">
                    <ul role="list">
                      <li>Мгновенный выбор изделий</li>
                      <li>Оценка функционального состояния</li>
                      <li>Индивидуальный план поддержки</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div role="listitem" class="bullet_item">
            <div class="flexbox_spec">
              <div class="flex_icon">
                <div class="circle_icon"><img src="/images/682508921becac2ff658f730_days-icon.avif" loading="lazy" alt=""/></div>
                <div class="title_pd"><div class="title_cms">В течение первых дней</div></div>
              </div>
              <div class="bullet_list">
                <div><div class="title_cms">Ощутимый эффект.</div></div>
                <div class="bullet_cms">
                  <div class="rich_bullet w-richtext">
                    <ul role="list">
                      <li>Заметное улучшение комфорта</li>
                      <li>Снижение нагрузки на суставы</li>
                      <li>Положительная динамика движения</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div role="listitem" class="bullet_item">
            <div class="flexbox_spec">
              <div class="flex_icon">
                <div class="circle_icon"><img src="/images/682508a5feb1f8706e0301cc_months-icon.avif" loading="lazy" alt=""/></div>
                <div class="title_pd"><div class="title_cms">В долгосрочной перспективе</div></div>
              </div>
              <div class="bullet_list">
                <div><div class="title_cms">Ваше здоровье в движении.</div></div>
                <div class="bullet_cms">
                  <div class="rich_bullet w-richtext">
                    <ul role="list">
                      <li>Восстановление активности</li>
                      <li>Устойчивый результат реабилитации</li>
                      <li>Надежная профилактика</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section data-w-id="bcaf909a-436f-c9a4-ab43-811ae0e3c023" class="cta_section">
  <div class="wrapper_cta">
    <div class="cta_headline">
      <h2 letters-slide-up="" text-split="" class="h2 cta_last">Основано на данных.<br/>Создано для жизни. <br/>Разработано для вас.</h2>
      <div class="desc_box">
        <div class="txt_base white">Станьте частью экспертной системы НИКАМЕД и получите доступ к инновационным решениям в области ортопедии.</div>
      </div>
      <div class="button_box">
        <a data-w-id="a3bba266-da0b-a874-ddbc-99cfcef833a3" href="#" class="button_link white_button white_white w-inline-block">
          <div>Для партнеров</div>
          <div class="circle_link black b_b">
            <div class="arrow_icon white first_arrow a_f"><img src="/images/6819ec297e6347786f9815eb_arrow_button.svg" loading="lazy" alt=""/></div>
            <div class="arrow_icon white second_arrow a_l"><img src="/images/6819ec297e6347786f9815eb_arrow_button.svg" loading="lazy" alt=""/></div>
          </div>
        </a>
      </div>
    </div>
  </div>
  <div class="background_image">
    <img src="/images/6824fdec131ae13dc2118401_cta_photo.avif" loading="lazy" sizes="(max-width: 6400px) 100vw, 6400px" srcset="/images/6824fdec131ae13dc2118401_cta_photo.avif 6400w" alt="Girl photo portrait, light depth, photo, avif" class="image"/>
  </div>
</section>
"""

if target in content:
    # We want to insert insertion BEFORE target
    new_content = content.replace(target, insertion + target, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("SUCCESS")
else:
    print("TARGET NOT FOUND")
