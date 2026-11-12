// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// MULTI-CHAPTER PORTAL CONTROLLER, QUIZ ENGINE, EXERCISE HUB, SLIDE & AUDIO PLAYER
// C# / .NET 8 (DEITEL & DEITEL - VISUAL C# HOW TO PROGRAM)
// ============================================================================

// State Management
const AppState = {
  currentTab: 'overview',
  currentChapter: 1,
  currentSlide: 1,
  totalSlides: 42,
  currentQuestionIndex: 0,
  quizFilter: 'all',
  userAnswers: {}, // questionId -> selectedOptionIndex
  exerciseFilter: 'all',
  theme: localStorage.getItem('theme') || 'light',
  isPlayingAudio: false
};

// ============================================================================
// DYNAMIC MULTI-CHAPTER DATA GETTERS
// ============================================================================
function getCurrentQuiz() {
  if (AppState.currentChapter === 2) {
    return (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];
  }
  return (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];
}

function getCurrentExercises() {
  if (AppState.currentChapter === 2) {
    return (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];
  }
  return (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];
}

function getCurrentTranscripts() {
  if (AppState.currentChapter === 2) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_02 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_02 : {};
  }
  if (typeof SLIDE_TRANSCRIPTS_CHAPTER_01 !== 'undefined') {
    return SLIDE_TRANSCRIPTS_CHAPTER_01;
  }
  if (typeof SLIDE_TRANSCRIPTS !== 'undefined') {
    return SLIDE_TRANSCRIPTS;
  }
  return {};
}

function getCurrentChapterMeta() {
  if (typeof CHAPTER_METADATA !== 'undefined' && CHAPTER_METADATA[AppState.currentChapter]) {
    return CHAPTER_METADATA[AppState.currentChapter];
  }
  return {
    id: 1,
    title: "Chương 1: Introduction to Computers, the Internet and Visual C#",
    heroTitle: "CHƯƠNG 1: INTRODUCTION TO COMPUTERS, THE INTERNET AND VISUAL C#",
    heroDesc: "Nền tảng hệ thống máy tính, định luật Moore, 6 khối chức năng logic, cấu trúc phân cấp dữ liệu, tiến hóa ngôn ngữ, công nghệ đối tượng (OOP), kiến trúc Microsoft .NET (CLR, MSIL, JIT), Visual Studio IDE và Test-Drive ứng dụng đồ họa tương tác Painter.",
    pills: [
      "⏱️ Thời lượng: 3 Tiết (150')",
      "🎯 5 Chuẩn đầu ra (CLO)",
      "📝 40 Câu trắc nghiệm chuẩn hóa",
      "💻 29 Bài tập giáo khoa & Making-a-Difference"
    ],
    totalSlides: 42,
    videoDir: "./VideoCShape/Chapter_01",
    slidePdf: "./VideoCShape/Chapter_01/Slide_Chapter_01.pdf",
    slideName: "Slide_Chapter_01.pdf"
  };
}

// ============================================================================
// INITIALIZATION
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initChapterSelector();
  initTabs();
  initSlidePlayer();
  initTheaterTranscript();
  initQuizEngine();
  initExerciseHub();
  initCodeRepository();
});

// ============================================================================
// THEME CONTROLLER
// ============================================================================
function initTheme() {
  if (AppState.theme === 'dark') {
    document.body.classList.add('dark-theme');
    updateThemeIcon('☀️');
  } else {
    document.body.classList.remove('dark-theme');
    updateThemeIcon('🌙');
  }

  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark-theme');
      const isDark = document.body.classList.contains('dark-theme');
      AppState.theme = isDark ? 'dark' : 'light';
      localStorage.setItem('theme', AppState.theme);
      updateThemeIcon(isDark ? '☀️' : '🌙');
    });
  }
}

function updateThemeIcon(icon) {
  const btn = document.getElementById('themeToggleBtn');
  if (btn) btn.textContent = icon;
}

// ============================================================================
// TAB NAVIGATION
// ============================================================================
function initTabs() {
  const tabBtns = document.querySelectorAll('.nav-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.getAttribute('data-tab');
      switchTab(targetTab);
    });
  });
}

function switchTab(tabId) {
  AppState.currentTab = tabId;

  // Update Buttons
  document.querySelectorAll('.nav-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Update Panes
  document.querySelectorAll('.tab-pane').forEach(pane => {
    if (pane.id === `tab-${tabId}`) {
      pane.classList.add('active');
    } else {
      pane.classList.remove('active');
    }
  });

  // Scroll to top of content smoothly
  window.scrollTo({ top: 120, behavior: 'smooth' });
}
window.switchTab = switchTab;

// ============================================================================
// CHAPTER SWITCHING CONTROLLER (MULTI-CHAPTER PORTAL)
// ============================================================================
function initChapterSelector() {
  const selector = document.getElementById('chapterSelector');
  if (selector) {
    const initialVal = parseInt(selector.value, 10);
    if (initialVal === 2) {
      switchChapter(2);
    } else {
      updateVideoTab(1);
    }

    selector.addEventListener('change', (e) => {
      switchChapter(e.target.value);
    });
  }
}

function updateVideoTab(chapterNum) {
  const meta = getCurrentChapterMeta();
  if (!meta) return;

  // 1. Iframe video player (Rạp chiếu to toàn màn hình)
  const iframe = document.getElementById('chapterVideoIframe');
  if (iframe) {
    const targetSrc = `./VideoCShape/Chapter_0${chapterNum}/index.html`;
    const normalizedSrc = iframe.src ? iframe.src.replace(/\\/g, '/') : '';
    if (!normalizedSrc.endsWith(`VideoCShape/Chapter_0${chapterNum}/index.html`)) {
      iframe.src = targetSrc;
    }
    iframe.title = `Trình phát Bài giảng Video Chương ${chapterNum}`;
  }

  // 2. Toolbar buttons in Tab 3
  const openPdfBtn = document.getElementById('videoTabOpenPdfBtn');
  if (openPdfBtn) {
    openPdfBtn.href = meta.slidePdf;
    openPdfBtn.innerHTML = `📄 Mở ${meta.slideName}`;
  }

  const openTabBtn = document.getElementById('videoTabOpenTabBtn');
  if (openTabBtn) {
    openTabBtn.href = `${meta.videoDir}/index.html`;
  }

  // 3. Theater top bar badge and buttons
  const badgeTitle = document.getElementById('theaterBadgeTitle');
  if (badgeTitle) {
    badgeTitle.textContent = `Trình phát Video Bài giảng Chương ${chapterNum} (Toàn màn hình Chuẩn Mặc Định)`;
  }

  const badgeSubtitle = document.getElementById('theaterBadgeSubtitle');
  if (badgeSubtitle) {
    badgeSubtitle.textContent = `${meta.slideName} • ${meta.totalSlides} Slide HD • C# .NET • Audio & Tự Động Chuyển Slide`;
  }

  const downloadPdfBtn = document.getElementById('theaterDownloadPdfBtn');
  if (downloadPdfBtn) {
    downloadPdfBtn.href = meta.slidePdf;
    downloadPdfBtn.innerHTML = `📥 Tải ${meta.slideName}`;
  }

  const fullscreenBtn = document.getElementById('theaterFullscreenTabBtn');
  if (fullscreenBtn) {
    fullscreenBtn.href = `${meta.videoDir}/index.html`;
  }

  // 4. Split view top bar
  const splitBadge = document.getElementById('splitSlideBadge');
  if (splitBadge) {
    splitBadge.textContent = `🎯 Slide: ${meta.slideName}`;
  }

  const splitCount = document.getElementById('splitSlideCount');
  if (splitCount) {
    splitCount.textContent = `(${meta.totalSlides} Trang HD)`;
  }

  // 5. Theater transcript section heading & script download
  const transcriptHeading = document.getElementById('theaterTranscriptHeading');
  if (transcriptHeading) {
    transcriptHeading.textContent = `Kịch bản Đối thoại Thuyết minh ${meta.totalSlides} Slide C# (Thầy & Trò IT26M)`;
  }

  const downloadScript = document.getElementById('downloadScriptBtn');
  if (downloadScript) {
    downloadScript.href = `${meta.videoDir}/script.txt`;
  }
}

function updateChapterStaticContent(chapterNum) {
  const meta = getCurrentChapterMeta();
  if (!meta) return;

  // Hero Banner Title
  const heroTitle = document.querySelector('.hero-banner h2');
  if (heroTitle && meta.heroTitle) {
    heroTitle.textContent = meta.heroTitle;
  }

  // Hero Banner Subtitle
  const heroDesc = document.querySelector('.hero-banner .hero-subtitle');
  if (heroDesc && meta.heroDesc) {
    heroDesc.textContent = meta.heroDesc;
  }

  // Hero Banner Meta Pills
  const heroMeta = document.querySelector('.hero-banner .hero-meta');
  if (heroMeta && meta.pills) {
    heroMeta.innerHTML = meta.pills.map(p => `<span>${p}</span>`).join('');
  }

  // Tab 1: Overview
  const tabOverview = document.getElementById('tab-overview');
  if (tabOverview && meta.overviewHtml) {
    tabOverview.innerHTML = meta.overviewHtml;
  }

  // Tab 2: Docs
  const tabDocs = document.getElementById('tab-docs');
  if (tabDocs && meta.docsHtml) {
    tabDocs.innerHTML = meta.docsHtml;
  }

  // Tab 3: Video Tab Elements & Iframe
  updateVideoTab(chapterNum);

  // Tab 6: Codes
  const tabCodes = document.getElementById('tab-codes');
  if (tabCodes && meta.codesHtml) {
    tabCodes.innerHTML = meta.codesHtml;
  }
}

function switchChapter(ch) {
  const chapterNum = parseInt(ch, 10);
  if (chapterNum !== 1 && chapterNum !== 2) return;

  AppState.currentChapter = chapterNum;
  const meta = getCurrentChapterMeta();
  AppState.totalSlides = meta.totalSlides;
  AppState.currentSlide = 1;
  AppState.currentQuestionIndex = 0;
  AppState.userAnswers = {};
  AppState.quizFilter = 'all';
  AppState.exerciseFilter = 'all';

  // Stop audio if currently playing
  const audioEl = document.getElementById('slideNarrationAudio');
  if (audioEl) {
    audioEl.pause();
    audioEl.currentTime = 0;
  }
  AppState.isPlayingAudio = false;
  const playAudioBtn = document.getElementById('slideAudioPlayBtn');
  if (playAudioBtn) {
    playAudioBtn.innerHTML = '▶️ Nghe Thuyết Minh';
    playAudioBtn.style.background = 'var(--accent-green)';
  }
  const audioStatus = document.getElementById('audioStatusText');
  if (audioStatus) {
    audioStatus.textContent = 'Sẵn sàng phát Slide 1';
  }

  // Synchronize selector options display text
  const selector = document.getElementById('chapterSelector');
  if (selector) {
    selector.value = chapterNum;
    if (selector.options) {
      for (let i = 0; i < selector.options.length; i++) {
        let opt = selector.options[i];
        let val = parseInt(opt.value, 10);
        let baseText = opt.textContent.replace(' (Đang mở)', '');
        if (val === chapterNum) {
          opt.textContent = `${baseText} (Đang mở)`;
        } else {
          opt.textContent = baseText;
        }
      }
    }
  }

  // Update static tab contents (Overview, Docs, Codes) & Hero Banner
  updateChapterStaticContent(chapterNum);

  // Re-populate slide dropdown options (1..42 or 1..45)
  populateSlideDropdowns();

  // Re-render slide player & transcript
  renderSlide(1);
  renderTheaterTranscript(1);

  // Re-render quiz engine
  renderQuizDashboard();
  renderQuestionPalette();
  renderCurrentQuestion();

  // Re-render exercise hub
  const searchInput = document.getElementById('exerciseSearchInput');
  if (searchInput) searchInput.value = '';
  renderExerciseList();

  // Reset filter buttons active state
  document.querySelectorAll('.quiz-filter-btn').forEach(b => {
    if (b.getAttribute('data-filter') === 'all') b.classList.add('active');
    else b.classList.remove('active');
  });
  document.querySelectorAll('.ex-filter-btn').forEach(b => {
    if (b.getAttribute('data-filter') === 'all') b.classList.add('active');
    else b.classList.remove('active');
  });
}
window.switchChapter = switchChapter;

// ============================================================================
// SLIDE & AUDIO NARRATION PLAYER
// ============================================================================
function populateSlideDropdowns() {
  const transcripts = getCurrentTranscripts();
  const slideSelect = document.getElementById('slideNumberSelect');
  const theaterSelect = document.getElementById('theaterTranscriptSlideSelect');

  if (slideSelect) {
    slideSelect.innerHTML = '';
    for (let i = 1; i <= AppState.totalSlides; i++) {
      const opt = document.createElement('option');
      opt.value = i;
      const title = transcripts[i]?.title || `Slide ${i}`;
      opt.textContent = `Slide ${i}: ${title.substring(0, 32)}...`;
      slideSelect.appendChild(opt);
    }
    slideSelect.value = AppState.currentSlide;
  }

  if (theaterSelect) {
    theaterSelect.innerHTML = '';
    for (let i = 1; i <= AppState.totalSlides; i++) {
      const opt = document.createElement('option');
      opt.value = i;
      const title = transcripts[i]?.title || `Slide ${i}`;
      opt.textContent = `Slide ${i}: ${title.substring(0, 36)}...`;
      theaterSelect.appendChild(opt);
    }
    theaterSelect.value = AppState.currentSlide;
  }
}

function initSlidePlayer() {
  populateSlideDropdowns();
  renderSlide(AppState.currentSlide);

  const prevBtn = document.getElementById('prevSlideBtn');
  const nextBtn = document.getElementById('nextSlideBtn');
  const slideSelect = document.getElementById('slideNumberSelect');

  if (slideSelect) {
    slideSelect.addEventListener('change', (e) => {
      renderSlide(parseInt(e.target.value, 10));
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (AppState.currentSlide > 1) {
        renderSlide(AppState.currentSlide - 1);
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (AppState.currentSlide < AppState.totalSlides) {
        renderSlide(AppState.currentSlide + 1);
      }
    });
  }

  // Audio Playback Controller
  const audioEl = document.getElementById('slideNarrationAudio');
  const playAudioBtn = document.getElementById('slideAudioPlayBtn');
  const audioStatus = document.getElementById('audioStatusText');
  const autoAdvanceCheck = document.getElementById('autoAdvanceAudioCheck');

  if (playAudioBtn && audioEl) {
    playAudioBtn.addEventListener('click', () => {
      if (audioEl.paused) {
        startOrResumeAudio();
      } else {
        pauseAudio();
      }
    });

    audioEl.addEventListener('play', () => {
      AppState.isPlayingAudio = true;
      playAudioBtn.innerHTML = '⏸️ Tạm Dừng';
      playAudioBtn.style.background = 'var(--accent-amber)';
      if (audioStatus) audioStatus.textContent = `Đang phát Slide ${AppState.currentSlide}...`;
    });

    audioEl.addEventListener('pause', () => {
      AppState.isPlayingAudio = false;
      playAudioBtn.innerHTML = '▶️ Tiếp Tục Nghe';
      playAudioBtn.style.background = 'var(--accent-green)';
      if (audioStatus) audioStatus.textContent = `Tạm dừng Slide ${AppState.currentSlide}`;
    });

    audioEl.addEventListener('timeupdate', () => {
      if (audioStatus && audioEl.duration) {
        const cur = formatTime(audioEl.currentTime);
        const dur = formatTime(audioEl.duration);
        audioStatus.textContent = `Đang phát Slide ${AppState.currentSlide} (${cur} / ${dur})`;
      }
    });

    audioEl.addEventListener('ended', () => {
      if (autoAdvanceCheck && autoAdvanceCheck.checked && AppState.currentSlide < AppState.totalSlides) {
        renderSlide(AppState.currentSlide + 1);
        playSlideAudio(AppState.currentSlide);
      } else {
        AppState.isPlayingAudio = false;
        playAudioBtn.innerHTML = '▶️ Nghe Lại Slide';
        playAudioBtn.style.background = 'var(--accent-green)';
        if (audioStatus) audioStatus.textContent = `Đã kết thúc Slide ${AppState.currentSlide}`;
      }
    });

    audioEl.addEventListener('error', () => {
      if (audioStatus) audioStatus.textContent = `Không có audio cho Slide ${AppState.currentSlide}`;
      AppState.isPlayingAudio = false;
      playAudioBtn.innerHTML = '▶️ Nghe Thuyết Minh';
      playAudioBtn.style.background = 'var(--accent-green)';
    });
  }

  // Keyboard navigation for slides
  document.addEventListener('keydown', (e) => {
    if (AppState.currentTab === 'video') {
      if (e.key === 'ArrowLeft' && AppState.currentSlide > 1) {
        renderSlide(AppState.currentSlide - 1);
      } else if (e.key === 'ArrowRight' && AppState.currentSlide < AppState.totalSlides) {
        renderSlide(AppState.currentSlide + 1);
      }
    }
  });
}

function formatTime(seconds) {
  if (isNaN(seconds)) return '00:00';
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
}

function startOrResumeAudio() {
  const audioEl = document.getElementById('slideNarrationAudio');
  if (!audioEl) return;
  const meta = getCurrentChapterMeta();
  const targetSrc = `${meta.videoDir}/audio/slide_${AppState.currentSlide}.mp3`;
  if (!audioEl.src.endsWith(`slide_${AppState.currentSlide}.mp3`)) {
    audioEl.src = targetSrc;
  }
  audioEl.play().catch(err => {
    console.warn("Audio autoplay blocked or failed:", err);
  });
}

function pauseAudio() {
  const audioEl = document.getElementById('slideNarrationAudio');
  if (audioEl) audioEl.pause();
}

function playSlideAudio(slideNum) {
  const audioEl = document.getElementById('slideNarrationAudio');
  if (!audioEl) return;
  const meta = getCurrentChapterMeta();
  audioEl.src = `${meta.videoDir}/audio/slide_${slideNum}.mp3`;
  audioEl.play().catch(err => console.warn(err));
}

function renderSlide(slideNum) {
  AppState.currentSlide = slideNum;
  const meta = getCurrentChapterMeta();
  const transcripts = getCurrentTranscripts();

  // Update Buttons & Counter
  const prevBtn = document.getElementById('prevSlideBtn');
  const nextBtn = document.getElementById('nextSlideBtn');
  const counter = document.getElementById('slideCounterText');
  const slideSelect = document.getElementById('slideNumberSelect');
  const theaterSelect = document.getElementById('theaterTranscriptSlideSelect');

  if (prevBtn) prevBtn.disabled = (slideNum === 1);
  if (nextBtn) nextBtn.disabled = (slideNum === AppState.totalSlides);
  if (counter) counter.textContent = `Slide ${slideNum} / ${AppState.totalSlides}`;
  if (slideSelect) slideSelect.value = slideNum;
  if (theaterSelect) theaterSelect.value = slideNum;

  // Render Slide Display
  const slideDisplay = document.getElementById('slideDisplayFrame');
  const transcriptData = transcripts[slideNum] || {
    title: `Slide ${slideNum}`,
    speaker1: "Nội dung thuyết minh giảng viên.",
    speaker2: "Phản hồi của sinh viên."
  };

  if (slideDisplay) {
    const visualHtml = `
      <div style="position: relative; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: #000;">
        <img src="${meta.videoDir}/images/slide-${slideNum}.png" 
             alt="Slide ${slideNum}: ${transcriptData.title}" 
             class="slide-image" 
             style="max-width: 100%; max-height: 100%; object-fit: contain; box-shadow: 0 4px 12px rgba(0,0,0,0.5);"
             onerror="this.onerror=null; this.parentElement.innerHTML='<div style=\'color:#fff;padding:2rem;text-align:center;\'>Không thể tải slide. <a href=\'${meta.slidePdf}\' target=\'_blank\' style=\'color:#38bdf8;\'>Bấm vào đây để mở ${meta.slideName}</a></div>';">
        <div style="position: absolute; bottom: 8px; right: 12px; background: rgba(0, 0, 0, 0.75); padding: 3px 10px; border-radius: 4px; font-size: 0.75rem; color: #38bdf8; font-weight: 600; pointer-events: none;">
          ${meta.slideName} (Trang ${slideNum}/${AppState.totalSlides})
        </div>
      </div>
    `;
    slideDisplay.innerHTML = visualHtml;
  }

  // Handle Audio transition if playing
  const audioEl = document.getElementById('slideNarrationAudio');
  const playAudioBtn = document.getElementById('slideAudioPlayBtn');
  const audioStatus = document.getElementById('audioStatusText');
  if (audioEl) {
    if (AppState.isPlayingAudio) {
      playSlideAudio(slideNum);
    } else {
      audioEl.src = `${meta.videoDir}/audio/slide_${slideNum}.mp3`;
      if (playAudioBtn) {
        playAudioBtn.innerHTML = '▶️ Nghe Thuyết Minh';
        playAudioBtn.style.background = 'var(--accent-green)';
      }
      if (audioStatus) {
        audioStatus.textContent = `Sẵn sàng phát Slide ${slideNum}`;
      }
    }
  }

  // Render Transcript Dialogue
  const transcriptBody = document.getElementById('transcriptDialogueBody');
  if (transcriptBody) {
    transcriptBody.innerHTML = `
      <div class="dialogue-item dialogue-speaker-1">
        <span class="speaker-label">👨‍🏫 Người 1 (Giảng viên)</span>
        <p>${transcriptData.speaker1}</p>
      </div>
      <div class="dialogue-item dialogue-speaker-2">
        <span class="speaker-label">🧑‍🎓 Người 2 (Sinh viên IT26M)</span>
        <p>${transcriptData.speaker2}</p>
      </div>
    `;
  }

  // Update theater transcript
  renderTheaterTranscript(slideNum);
}

// ============================================================================
// THEATER VIEW & TRANSCRIPT CONTROLLER
// ============================================================================
function setVideoViewMode(mode) {
  const theaterContainer = document.getElementById('theaterPlayerContainer');
  const splitContainer = document.getElementById('splitPlayerContainer');
  const theaterBtn = document.getElementById('viewModeTheaterBtn');
  const splitBtn = document.getElementById('viewModeSplitBtn');

  if (mode === 'theater') {
    if (theaterContainer) theaterContainer.style.display = 'block';
    if (splitContainer) splitContainer.style.display = 'none';
    if (theaterBtn) theaterBtn.classList.add('active');
    if (splitBtn) splitBtn.classList.remove('active');
  } else {
    if (theaterContainer) theaterContainer.style.display = 'none';
    if (splitContainer) splitContainer.style.display = 'grid';
    if (theaterBtn) theaterBtn.classList.remove('active');
    if (splitBtn) splitBtn.classList.add('active');
  }
}
window.setVideoViewMode = setVideoViewMode;

function initTheaterTranscript() {
  const selectEl = document.getElementById('theaterTranscriptSlideSelect');
  if (!selectEl) return;

  selectEl.addEventListener('change', (e) => {
    renderTheaterTranscript(parseInt(e.target.value, 10));
  });

  renderTheaterTranscript(AppState.currentSlide);
}

function renderTheaterTranscript(slideNum) {
  const bodyEl = document.getElementById('theaterTranscriptBody');
  if (!bodyEl) return;
  const meta = getCurrentChapterMeta();
  const transcripts = getCurrentTranscripts();

  const data = transcripts[slideNum] || {
    title: `Slide ${slideNum}`,
    speaker1: "Nội dung thuyết minh giảng viên.",
    speaker2: "Phản hồi của sinh viên."
  };

  bodyEl.innerHTML = `
    <div style="margin-bottom: 1rem; padding: 0.75rem 1rem; background: var(--primary-light); border-radius: 6px; font-weight: 700; color: var(--primary-navy); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
      <span>📌 Lời thoại Slide ${slideNum}: ${data.title}</span>
      <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-muted);">Trích xuất từ ${meta.videoDir}/script.txt</span>
    </div>
    <div class="transcript-dialogue-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem;">
      <div class="dialogue-item dialogue-speaker-1" style="height: 100%;">
        <span class="speaker-label">👨‍🏫 Người 1 (Giảng viên)</span>
        <p style="margin-top: 0.5rem; line-height: 1.6;">${data.speaker1}</p>
      </div>
      <div class="dialogue-item dialogue-speaker-2" style="height: 100%;">
        <span class="speaker-label">🧑‍🎓 Người 2 (Sinh viên IT26M)</span>
        <p style="margin-top: 0.5rem; line-height: 1.6;">${data.speaker2}</p>
      </div>
    </div>
  `;
}

// ============================================================================
// QUIZ ENGINE (40 CÂU HỎI TRẮC NGHIỆM CHUẨN HÓA)
// ============================================================================
function initQuizEngine() {
  renderQuizDashboard();
  renderQuestionPalette();
  renderCurrentQuestion();

  // Navigation Buttons
  const prevBtn = document.getElementById('prevQuestionBtn');
  const nextBtn = document.getElementById('nextQuestionBtn');
  const resetBtn = document.getElementById('resetQuizBtn');

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (AppState.currentQuestionIndex > 0) {
        AppState.currentQuestionIndex--;
        renderCurrentQuestion();
        renderQuestionPalette();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      const quiz = getCurrentQuiz();
      if (AppState.currentQuestionIndex < quiz.length - 1) {
        AppState.currentQuestionIndex++;
        renderCurrentQuestion();
        renderQuestionPalette();
      }
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      const quiz = getCurrentQuiz();
      if (confirm(`Bạn có chắc chắn muốn làm lại từ đầu toàn bộ ${quiz.length} câu hỏi trắc nghiệm?`)) {
        AppState.userAnswers = {};
        AppState.currentQuestionIndex = 0;
        renderQuizDashboard();
        renderQuestionPalette();
        renderCurrentQuestion();
      }
    });
  }

  // Filter Buttons
  const filterBtns = document.querySelectorAll('.quiz-filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      AppState.quizFilter = btn.getAttribute('data-filter');
      renderQuestionPalette();
    });
  });
}

function renderQuizDashboard() {
  const quiz = getCurrentQuiz();
  const total = quiz.length;
  let correctCount = 0;
  let answeredCount = 0;

  quiz.forEach(q => {
    if (AppState.userAnswers.hasOwnProperty(q.id)) {
      answeredCount++;
      if (AppState.userAnswers[q.id] === q.correct) {
        correctCount++;
      }
    }
  });

  const progressPct = total > 0 ? Math.round((answeredCount / total) * 100) : 0;
  const scorePct = (total > 0 && answeredCount > 0) ? Math.round((correctCount / total) * 100) : 0;

  // DOM Elements
  const statProgress = document.getElementById('quizStatProgress');
  const statScore = document.getElementById('quizStatScore');
  const statAccuracy = document.getElementById('quizStatAccuracy');
  const progressBar = document.getElementById('quizProgressBar');

  if (statProgress) statProgress.textContent = `${answeredCount} / ${total}`;
  if (statScore) statScore.textContent = `${correctCount} câu đúng`;
  if (statAccuracy) statAccuracy.textContent = `${scorePct}% (${total > 0 ? (correctCount * 10 / total).toFixed(1) : 0} / 10)`;
  if (progressBar) progressBar.style.width = `${progressPct}%`;
}

function renderQuestionPalette() {
  const palette = document.getElementById('quizQuestionPalette');
  if (!palette) return;

  palette.innerHTML = '';
  const quiz = getCurrentQuiz();
  quiz.forEach((q, idx) => {
    const isAnswered = AppState.userAnswers.hasOwnProperty(q.id);
    const isCorrect = isAnswered && (AppState.userAnswers[q.id] === q.correct);
    const isIncorrect = isAnswered && !isCorrect;

    // Filter logic
    if (AppState.quizFilter === 'correct' && !isCorrect) return;
    if (AppState.quizFilter === 'incorrect' && !isIncorrect) return;
    if (AppState.quizFilter === 'unanswered' && isAnswered) return;

    const btn = document.createElement('button');
    btn.className = 'palette-btn';
    btn.textContent = q.id;

    if (idx === AppState.currentQuestionIndex) btn.classList.add('current');
    if (isCorrect) btn.classList.add('correct');
    if (isIncorrect) btn.classList.add('incorrect');

    btn.addEventListener('click', () => {
      AppState.currentQuestionIndex = idx;
      renderCurrentQuestion();
      renderQuestionPalette();
    });

    palette.appendChild(btn);
  });
}

function renderCurrentQuestion() {
  const quiz = getCurrentQuiz();
  const q = quiz[AppState.currentQuestionIndex];
  if (!q) return;

  const card = document.getElementById('quizQuestionCard');
  if (!card) return;

  const isAnswered = AppState.userAnswers.hasOwnProperty(q.id);
  const selectedIndex = isAnswered ? AppState.userAnswers[q.id] : null;

  // Prev / Next button states
  const prevBtn = document.getElementById('prevQuestionBtn');
  const nextBtn = document.getElementById('nextQuestionBtn');
  if (prevBtn) prevBtn.disabled = (AppState.currentQuestionIndex === 0);
  if (nextBtn) nextBtn.disabled = (AppState.currentQuestionIndex === quiz.length - 1);

  // Question HTML
  const letters = ['A', 'B', 'C', 'D'];
  const optionsHtml = q.options.map((optText, optIdx) => {
    let btnClass = 'option-btn';
    if (isAnswered) {
      if (optIdx === q.correct) {
        btnClass += ' selected-correct';
      } else if (optIdx === selectedIndex) {
        btnClass += ' selected-incorrect';
      }
    }

    return `
      <button class="${btnClass}" ${isAnswered ? 'disabled' : ''} onclick="handleSelectOption(${q.id}, ${optIdx})">
        <span class="option-letter">${letters[optIdx]}</span>
        <span class="option-text">${optText}</span>
      </button>
    `;
  }).join('');

  card.innerHTML = `
    <div class="question-meta-tags">
      <span class="tag-badge tag-category">${q.category}</span>
      <span class="tag-badge tag-bloom">Bloom: ${q.bloom}</span>
      <span class="tag-badge" style="background: var(--bg-subtle);">Câu ${q.id} / ${quiz.length}</span>
    </div>
    <h4 class="question-text">${q.question.replace(/\n/g, '<br>')}</h4>
    <div class="options-container">
      ${optionsHtml}
    </div>
    <div class="explanation-card ${isAnswered ? 'show' : ''}">
      <h5>💡 Giải thích chi tiết từ Giảng viên:</h5>
      <p>${q.explanation}</p>
    </div>
  `;
}

window.handleSelectOption = function(questionId, optionIndex) {
  AppState.userAnswers[questionId] = optionIndex;
  renderQuizDashboard();
  renderQuestionPalette();
  renderCurrentQuestion();
};

// ============================================================================
// EXERCISES HUB (BÀI TẬP CUỐI CHƯƠNG)
// ============================================================================
function initExerciseHub() {
  renderExerciseList();

  const filterBtns = document.querySelectorAll('.ex-filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      AppState.exerciseFilter = btn.getAttribute('data-filter');
      renderExerciseList();
    });
  });

  const searchInput = document.getElementById('exerciseSearchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      renderExerciseList(e.target.value.toLowerCase().trim());
    });
  }
}

function renderExerciseList(searchKeyword = '') {
  const container = document.getElementById('exerciseListContainer');
  if (!container) return;

  const exercises = getCurrentExercises();

  // Cập nhật số lượng bài tập động trên các nút filter
  const countAll = exercises.length;
  const countSelfReview = exercises.filter(e => e.type === 'self-review').length;
  const countExercises = exercises.filter(e => e.type === 'exercises').length;
  const countProjects = exercises.filter(e => e.type === 'making-a-difference').length;

  const btnAll = document.getElementById('exFilterAll');
  if (btnAll) btnAll.textContent = `Tất cả bài tập (${countAll})`;
  const btnSR = document.getElementById('exFilterSelfReview');
  if (btnSR) btnSR.textContent = `Self-Review (${countSelfReview})`;
  const btnEx = document.getElementById('exFilterExercises');
  if (btnEx) btnEx.textContent = `Exercises (${countExercises})`;
  const btnProj = document.getElementById('exFilterProjects');
  if (btnProj) btnProj.textContent = `Making-a-Difference (${countProjects})`;

  const filtered = exercises.filter(item => {
    const matchFilter = (AppState.exerciseFilter === 'all') || (item.type === AppState.exerciseFilter);
    const matchSearch = !searchKeyword || 
      item.title.toLowerCase().includes(searchKeyword) ||
      (item.number && item.number.toLowerCase().includes(searchKeyword)) ||
      (item.description && item.description.toLowerCase().includes(searchKeyword));
    return matchFilter && matchSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 3rem; color: var(--text-muted); background: var(--bg-surface); border-radius: var(--radius-lg); border: 1px dashed var(--border-color);">
        <p style="font-size: 1.1rem; font-weight: 600;">Không tìm thấy bài tập nào phù hợp với bộ lọc!</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(item => {
    let badgeClass = 'ex-badge-self-check';
    let badgeLabel = 'Self-Review';
    if (item.type === 'exercises') {
      badgeClass = 'ex-badge-exercise';
      badgeLabel = 'Exercise';
    } else if (item.type === 'making-a-difference') {
      badgeClass = 'ex-badge-project';
      badgeLabel = 'Making a Difference (Đồ án GUI)';
    }

    const starter = item.starterCode || item.code;
    const hasStarter = Boolean(starter);
    const hasExpected = Boolean(item.expectedOutput);
    const solutionOrAnswer = item.solutionCode || item.answer || item.solution || '';
    const hintText = item.hint || item.hints || '';
    const numberText = item.number || ('Bài ' + item.id);
    const pageText = item.page ? ` (Trang ${item.page})` : '';

    const config = (typeof INTERACTIVE_EXERCISES_DATA !== 'undefined') ? INTERACTIVE_EXERCISES_DATA[item.id] : null;
    
    // Rút gọn mô tả nếu bài tập đã có các câu hỏi chi tiết trong workspace
    let introDesc = item.description || item.question || '';
    if (config && (config.mode === 'fill-blank' || config.mode === 'true-false' || config.mode === 'concepts')) {
      const lines = introDesc.split('\n');
      const introLines = [];
      for (const line of lines) {
        if (/^[a-z0-9][\).]/i.test(line.trim())) break;
        introLines.push(line);
      }
      introDesc = introLines.join('\n').trim();
    }
    const descText = introDesc ? introDesc.replace(/\n/g, '<br>') : '';

    // Lấy thông tin trạng thái nộp bài của sinh viên từ LocalStorage
    const submission = (typeof getStoredExerciseSubmissions === 'function') 
      ? (getStoredExerciseSubmissions()[item.id] || null) 
      : null;
    let statusBadge = '';
    if (submission) {
      if (submission.score !== undefined && config && config.items) {
        const pct = Math.round((submission.score / config.items.length) * 100);
        const color = pct >= 80 ? '#10b981' : (pct >= 50 ? '#f59e0b' : '#ef4444');
        statusBadge = `<span style="font-size: 0.75rem; font-weight: 700; color: white; background: ${color}; padding: 0.15rem 0.5rem; border-radius: 999px;">🎯 Đã nộp: ${submission.score}/${config.items.length} (${pct}%)</span>`;
      } else {
        statusBadge = `<span style="font-size: 0.75rem; font-weight: 700; color: white; background: #10b981; padding: 0.15rem 0.5rem; border-radius: 999px;">✅ Đã làm bài</span>`;
      }
    }

    // Tạo khu vực làm bài tương tác trực tiếp
    const interactiveHtml = (typeof generateInteractiveWorkspace === 'function') 
      ? generateInteractiveWorkspace(item) 
      : '';

    return `
      <div class="exercise-card" id="card-${item.id}">
        <div class="exercise-card-header">
          <div class="exercise-title-group">
            <div style="display: flex; gap: 0.5rem; align-items: center; margin-bottom: 0.35rem; flex-wrap: wrap;">
              <span class="ex-badge ${badgeClass}">${badgeLabel}</span>
              <span style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted);">${numberText}${pageText}</span>
              <span style="font-size: 0.8rem; color: var(--text-muted);">• ${item.category || ''}</span>
              ${statusBadge}
            </div>
            <h4>${item.title}</h4>
          </div>
        </div>
        
        ${descText ? `<p class="exercise-desc">${descText}</p>` : ''}
        ${item.image ? `<div style="text-align: center; margin: 0.75rem 0;"><img src="${item.image}" alt="${item.title}" style="max-width: 100%; max-height: 380px; object-fit: contain; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);" onerror="this.parentElement.style.display='none';"><div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Hình minh họa giáo trình Deitel & Deitel</div></div>` : ''}
        
        ${hintText ? `<div style="font-size: 0.85rem; color: var(--primary-cyan); background: var(--primary-light); padding: 0.6rem 0.85rem; border-radius: var(--radius-sm); margin-bottom: 0.75rem;"><strong>💡 Gợi ý:</strong> ${hintText}</div>` : ''}

        ${hasExpected ? `
          <div style="margin-top: 0.5rem;">
            <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted);">Kết quả xuất mong đợi (Console Output):</span>
            <div class="expected-output-box">${escapeHtml(item.expectedOutput)}</div>
          </div>
        ` : ''}

        ${hasStarter ? `
          <div style="margin-top: 0.5rem;">
            <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted);">Khung mã nguồn khởi tạo (Starter Code):</span>
            <div class="code-container">
              <button class="btn-copy-code" onclick="copyCode(this, \`${escapeJsString(starter)}\`)">📋 Copy Code</button>
              <pre class="code-block"><code>${escapeHtml(starter)}</code></pre>
            </div>
          </div>
        ` : ''}

        <!-- KHU VỰC LÀM BÀI TRỰC TIẾP TRÊN WEB CỦA SINH VIÊN -->
        ${interactiveHtml}

        <!-- ĐÁP ÁN CHUẨN MẪU & PHÂN TÍCH TỪ GIÁO TRÌNH -->
        <div style="margin-top: 1.25rem;">
          <button class="solution-toggle-btn" onclick="toggleSolution('${item.id}')">
            <span>📖 Xem lời giải chuẩn & phân tích chi tiết từ giáo trình</span>
          </button>
          <div id="solution-${item.id}" class="solution-content">
            <div class="code-container">
              <button class="btn-copy-code" onclick="copyCode(this, \`${escapeJsString(solutionOrAnswer)}\`)">📋 Copy Lời giải</button>
              <pre class="code-block" style="border-left: 4px solid var(--accent-green); background: #0f172a;"><code>${escapeHtml(solutionOrAnswer)}</code></pre>
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

window.toggleSolution = function(id) {
  const el = document.getElementById(`solution-${id}`);
  if (el) el.classList.toggle('open');
};

window.copyCode = function(btn, text) {
  navigator.clipboard.writeText(text).then(() => {
    const originalText = btn.innerHTML;
    btn.innerHTML = '✅ Đã sao chép!';
    btn.style.background = '#10B981';
    setTimeout(() => {
      btn.innerHTML = originalText;
      btn.style.background = '';
    }, 2000);
  });
};

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function escapeJsString(str) {
  if (!str) return '';
  return str.replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\$/g, '\\$');
}

// ============================================================================
// CODE REPOSITORY MODAL / INLINE VIEWER
// ============================================================================
function initCodeRepository() {
  // Ready for code viewer enhancements
}
