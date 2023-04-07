;(function() {
	'use strict'

	class ScrollBox {

		static SCROLLER_HEIGHT_MIN = 25;

		constructor(container) {
			this.viewport = container.querySelector('.CI-viewport');
			this.contentBox = container.querySelector('.CI-content-box');
			this.pressed = false;
			this.init();
		}


		init() {
			this.viewportHeight = this.viewport.offsetHeight;
			this.contentHeight = this.contentBox.scrollHeight;
			if (this.viewportHeight >= this.contentHeight) return;

			this.max = this.viewport.clientHeight - this.contentHeight;
			this.ratio = this.viewportHeight / this.contentHeight;
			this.createScrollbar();
			this.registerEventsHandler();
		}

		createScrollbar() {
			const scrollbar = document.createElement('div'),
				scroller = document.createElement('div');

			scrollbar.className = 'scrollbar';
			scroller.className = 'scroller';

			scrollbar.appendChild(scroller);
			this.viewport.appendChild(scrollbar);

			this.scroller = this.viewport.querySelector('.scroller');
			this.scrollerHeight = parseInt(this.ratio * this.viewportHeight);
			this.scrollerHeight = (this.scrollerHeight <= ScrollBox.SCROLLER_HEIGHT_MIN) ? ScrollBox.SCROLLER_HEIGHT_MIN : this.scrollerHeight;
			this.scroller.style.height = this.scrollerHeight + 'px';
		}

		registerEventsHandler(e) {
			this.contentBox.addEventListener('scroll', () => {
				this.scroller.style.top = (this.contentBox.scrollTop * this.ratio) + 'px';
			});

			this.scroller.addEventListener('mousedown', e => {
				this.start = e.clientY;
				this.pressed = true;
			});

			document.addEventListener('mousemove', this.drop.bind(this));

			document.addEventListener('mouseup', () => this.pressed = false);
		}

		drop(e) {
			e.preventDefault();
			if (this.pressed === false) return;

			let shiftScroller = this.start - e.clientY;
			this.scroller.style.top = (this.scroller.offsetTop - shiftScroller) + 'px';

			let shiftContent = this.scroller.offsetTop / this.ratio;
			const totalheightScroller = this.scroller.offsetHeight + this.scroller.offsetTop;
			const maxOffsetScroller = this.viewportHeight - this.scroller.offsetHeight;

			if (this.scroller.offsetTop < 0) this.scroller.style.top = '0px';
			if (totalheightScroller >= this.viewportHeight) this.scroller.style.top = maxOffsetScroller + 'px';

			this.contentBox.scrollTo(0, shiftContent);
			this.start = e.clientY;
		}
	}

	const containers = document.querySelectorAll('.CI-container');
	for (let container of containers) {
		const scrollbox = new ScrollBox(container);
	}
})();