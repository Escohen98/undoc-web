/*
 * Copyright © Eric Cohen 2023
 * Script to toggle key button.
 */

(function() {
    window.addEventListener("load", initialize)

  //Initializes key button
  function initialize() {
    document.getElementById("key-button").addEventListener("mouseover", toggleKey);
    document.getElementById("key-button").addEventListener("mouseout", toggleKey);
    buildToolTip()
  }

  /*
   * Toggles the key's hidden state
   * I know there's a toggle function, but I can't find it,
   * so I'm going to use reverse logic
   */
  function toggleKey() {
    //Key div
    key = document.getElementById("keys");
    key.hidden = !key.hidden
  }

  //Found this online. Lost the link.
   //Creates a tooltip for the spans
   function buildToolTip() {
       var spans = document.getElementsByTagName('span');

       for (var i = 0; i < spans.length; i++) {
           var span = spans[i];
           var tooltip = createTooltip();

           span.addEventListener('mouseover', function(event) {
               var tag = this.className;
               var description = getDescription(tag);
               tooltip.innerHTML = this.innerHTML + ': ' + description;
               tooltip.style.display = 'block';
               positionTooltip(tooltip, event.clientX, event.clientY);
           });

           span.addEventListener('mousemove', function(event) {
               positionTooltip(tooltip, event.clientX, event.clientY);
           });

           span.addEventListener('mouseout', function(event) {
               tooltip.style.display = 'none';
           });

           span.appendChild(tooltip);
       }
   }

   function createTooltip() {
       var tooltip = document.createElement('div');
       tooltip.style.display = 'none';
       tooltip.style.position = 'fixed';
       tooltip.style.background = '#eee';
       tooltip.style.border = '1px solid #333';
       tooltip.style.padding = '5px';
       tooltip.style.zIndex = '1000';
       return tooltip;
   }

   function positionTooltip(tooltip, clientX, clientY) {
       tooltip.style.left = (clientX + 10) + 'px'; // Adjust the left position as needed
       tooltip.style.top = (clientY + 10) + 'px'; // Adjust the top position as needed
   }

  /*
   * Get each word description.
   * This is going to be fun...
   */
   function getDescription(tag) {
     let description = "";
     switch(tag) {
        case 'CC':
            description = 'Coordinating Conjunction';
            break;
        case 'LS':
            description = 'List Item Marker';
            break;
        case 'MD':
            description = 'Modal';
            break;
        case 'RP':
            description = 'Particle';
            break;
        case 'TO':
            description = '"to" as Preposition or Infinitive';
            break;
        case 'CD':
            description = 'Cardinal Number';
            break;
        case 'PRP':
            description = 'Personal Pronoun';
            break;
        case 'PRP$':
            description = 'Possessive Pronoun';
            break;
        case 'WP':
            description = 'Wh-Pronoun';
            break;
        case 'DT':
            description = 'Determiner';
            break;
        case 'PDT':
            description = 'Predeterminer';
            break;
        case 'POS':
            description = 'Possessive Ending';
            break;
        case 'WDT':
            description = 'Wh-Determiner';
            break;
        case 'EX':
            description = 'Existential There';
            break;
        case 'UH':
            description = 'Interjection';
            break;
        case 'JJ':
            description = 'Adjective';
            break;
        case 'JJR':
            description = 'Adjective, Comparative';
            break;
        case 'JJS':
            description = 'Adjective, Superlative';
            break;
        case 'RB':
            description = 'Adverb';
            break;
        case 'RBR':
            description = 'Adverb, Comparative';
            break;
        case 'RBS':
            description = 'Adverb, Superlative';
            break;
        case 'WRB':
            description = 'Wh-Adverb';
            break;
        case 'NN':
            description = 'Noun, Singular or Mass';
            break;
        case 'NNP':
            description = 'Proper Noun, Singular';
            break;
        case 'NNS':
            description = 'Noun, Plural';
            break;
        case 'VB':
            description = 'Verb, Base Form';
            break;
        case 'VBD':
            description = 'Verb, Past Tense';
            break;
        case 'VBG':
            description = 'Verb, Gerund or Present Participle';
            break;
        case 'VBN':
            description = 'Verb, Past Participle';
            break;
        case 'VBP':
            description = 'Verb, Non-3rd Person Singular Present';
            break;
        case 'VBZ':
            description = 'Verb, 3rd Person Singular Present';
            break;
        default:
            description = 'This tag is not recognized.';
      }
      return description;
   }

})();
